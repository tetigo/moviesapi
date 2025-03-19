# from django.shortcuts import render
from rest_framework import generics, views, permissions, response, status
from movies.models import Movie
from movies.serializers import (
    MovieListDetailSerializer,
    MovieModelSerializer,
    MovieStarsSerializer,
)
from app.permissions import GlobalDefaultPermission
from django.db.models import Count, Avg
from reviews.models import Review


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    permission_classes = [permissions.IsAuthenticated, GlobalDefaultPermission]

    def get_serializer_class(self):  # type: ignore
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    permission_classes = [permissions.IsAuthenticated, GlobalDefaultPermission]

    def get_serializer_class(self):  # type: ignore
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, GlobalDefaultPermission]
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values("genre__name").annotate(
            count=Count("id")
        )
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg("stars"))["avg_stars"]

        data = {
            "total_movies": total_movies,
            "total_reviews": total_reviews,
            "movies_by_genre": movies_by_genre,
            "average_starts": round(average_stars, 1) if average_stars else 0,
        }
        serializer = MovieStarsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return response.Response(
            data=serializer.validated_data, status=status.HTTP_200_OK
        )
