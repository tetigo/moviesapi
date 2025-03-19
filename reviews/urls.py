from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail-update-delete-view'),

]
