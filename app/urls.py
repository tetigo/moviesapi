"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# from genres.views import GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView
# from actors.views import ActorListCreateAPIView, ActorRetrieveUpdateDestroyAPIView
# from movies.views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView
# from reviews.views import ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("genres.urls")),
    # path('genres/', GenreListCreateAPIView.as_view(), name='genre-create-list'),
    # path('genres/<int:pk>/', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-detail-update-delete-view'),
    path("api/v1/", include("actors.urls")),
    # path('actors/', ActorListCreateAPIView.as_view(), name='actor-create-list'),
    # path('actors/<int:pk>/', ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor-detail-update-delete-view'),
    path("api/v1/", include("movies.urls")),
    # path('movies/', MovieListCreateAPIView.as_view(), name='movie-create-list'),
    # path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail-update-delete-view'),
    path("api/v1/", include("reviews.urls")),
    # path('reviews/', ReviewListCreateAPIView.as_view(), name='review-create-list'),
    # path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail-update-delete-view'),
    path("api/v1/", include("authentication.urls")),
]
