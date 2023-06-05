from django.shortcuts import render, redirect
from .models import Client, Order, Package, Country, Hotel
from .forms import LoginForm, SignupForm, PackageForm, ClientForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate
import requests

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about_us(request):
    response = requests.get('https://api.chucknorris.io/jokes/random').json()
    context = {'response': response}
    return render(request, 'about_us.html', context)

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

def order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'order_list.html', context)

#detail
def package_detail(request, package_id):
    package = Package.objects.get(pk=package_id)
    return render(request, 'package_detail.html', {'package': package})

#signup
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context,)

#crud operations
def create_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PackageForm()
    
    context = {'form': form}
    return render(request, 'create_package.html', context)

def update_package(request, package_id):
    package = Package.objects.get(id=package_id)
    countries = Country.objects.all()
    hotels = Hotel.objects.all()
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('package_detail', package_id=package_id)
    else:
        form = PackageForm(instance=package)

    context = {'form': form, 'package': package, 'countries': countries, 'hotels': hotels}
    return render(request, 'update_package.html', context)

def delete_package(request, package_id):
    package = Package.objects.get(id=package_id)
    if request.method == 'POST':
        package.delete()
        return redirect('home')

    return redirect('package_list')

#order
def create_order(request, package_id):
    package = Package.objects.get(id=package_id)

    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client = client_form.save()
            order = Order.objects.create(client=client, package=package)
            return redirect('package_detail', package_id=package_id)
    else:
        client_form = ClientForm()

    context = {'client_form': client_form, 'package': package}
    return render(request, 'create_order.html', context)

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    context = {'order': order}
    return render(request, 'order_detail.html', context)