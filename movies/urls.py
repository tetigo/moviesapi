from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListCreateAPIView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail-update-delete-view'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movie-stats-view'),

]
