from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .models import Hotel
from .models import rooms
from .models import Booking
# Create your views here.

def home_view(request):
    return render(request,'index.html')


def home_about(request):
    return render(request, 'about.html')


def home_services(request):
    return render(request, 'services.html')

def home_contact(request):
    return render(request, 'contact.html')


