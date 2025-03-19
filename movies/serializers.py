from rest_framework import serializers
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer
from movies.models import Movie

# from genres.models import Genre
# from actors.models import Actor
# from reviews.models import Review

from django.db.models import Avg

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(
#         queryset = Genre.objects.all()
#     )
#     release_date = serializers.DateField()
#     actors = serializers.PrimaryKeyRelatedField(
#         queryset = Actor.objects.all(),
#         many=True
#     )
#     resume=serializers.CharField()


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError(
                "Data de lançamento não pode ser anterior a 1990"
            )
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(
                "Resumo não deve ser maior que 200 caracteres"
            )


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "genre", "actors", "release_date", "rate", "resume"]

    def get_rate(self, obj):
        # reviews=obj.reviews.all()
        # if reviews:
        #     sum_reviews=0

        #     for review in reviews:
        #         sum_reviews+=review.stars
        #     reviews_count=reviews.count()
        #     print(sum_reviews, reviews_count, sum_reviews / reviews_count)
        #     return round(sum_reviews/reviews_count, 1)
        # return None
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return rate
        return None


class MovieStarsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_starts = serializers.FloatField()
