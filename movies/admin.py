from django.contrib import admin
from movies.models import Movie

# from actors.models import Actor

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "genre", "release_date", "resume")

    # def actors_list(self,obj):
    #     return " ,".join([actor.name for actor in obj.actors.all()])
