from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name="reviews")
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, "Valor minimo é 0"),
            MaxValueValidator(5, "Valor maximo é 5"),
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie.title
