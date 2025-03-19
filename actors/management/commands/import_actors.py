import csv
from datetime import datetime
from typing import Any
from django.core.management.base import BaseCommand, CommandParser

from actors.models import Actor


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        # return super().add_arguments(parser)
        parser.add_argument(
            "file_name",
            type=str,
            help="Nome do arquivo com atores",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        # return super().handle(*args, **options)
        file_name = options["file_name"]

        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                date = row["birthday"].strip()
                birthday = datetime.strptime(date, "%Y-%m-%d")
                nationality = row["nationality"]

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(
                    name=name, birthday=birthday, nationality=nationality
                )

        self.stdout.write(self.style.SUCCESS("ATORES IMPORTADOS COM SUCESSO!"))
