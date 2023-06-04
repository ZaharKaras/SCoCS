from django.urls import path
from .views import home, destination_list, hotel_list, package_list, package_detail

urlpatterns = [
    path('', home, name='home'),
    path('destinations/', destination_list, name='destination_list'),
    path('hotels/', hotel_list, name='hotel_list'),
    path('packages/', package_list, name='package_list'),
    path('packages/package/<int:package_id>/', package_detail, name='package_detail'),

]