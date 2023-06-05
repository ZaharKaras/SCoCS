from django.urls import path, include
from .views import home, destination_list, hotel_list, package_list, package_detail, signup, create_package, delete_package, update_package, create_order
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('destinations/', destination_list, name='destination_list'),
    path('hotels/', hotel_list, name='hotel_list'),
    path('packages/', package_list, name='package_list'),
    path('packages/package/<int:package_id>/', package_detail, name='package_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('packages/create/', create_package, name='create_package'),
    path('packages/delete/<int:package_id>/', delete_package, name='delete_package'),
    path('packages/update/<int:package_id>/', update_package, name='update_package'),
    path('packages/<int:package_id>/create_order/', create_order, name='create_order')
]