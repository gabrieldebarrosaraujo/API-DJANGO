from django.urls import path
from .views import CarListAPIView, CarDetailAPIView, cars_list, car_detail

urlpatterns = [
    # Class-Based Views
    path('cars/', CarListAPIView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailAPIView.as_view(), name='car-detail'),

    # Function-Based Views
    path('fbv/cars/', cars_list, name='cars-list-fbv'),
    path('fbv/cars/<int:pk>/', car_detail, name='car-detail-fbv'),
]
