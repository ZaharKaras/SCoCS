from django.shortcuts import render
from .models import Client, Order, Package, Country, Hotel
# Create your views here.


def home(request):
    return render(request, 'home.html')

#view 
def destination_list(request):
    countries = Country.objects.all()
    return render(request, 'destination_list.html', {'countries': countries})

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

def package_list(request):
    packages = Package.objects.all()
    return render(request, 'package_list.html', {'packages': packages})

#detail
def package_detail(request, package_id):
    package = Package.objects.get(pk=package_id)
    return render(request, 'package_detail.html', {'package': package})