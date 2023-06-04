from django.urls import path, include
from .views import home, destination_list, hotel_list, package_list, package_detail, signup
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('destinations/', destination_list, name='destination_list'),
    path('hotels/', hotel_list, name='hotel_list'),
    path('packages/', package_list, name='package_list'),
    path('packages/package/<int:package_id>/', package_detail, name='package_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', signup, name='signup')
]