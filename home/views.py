from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .models import Hotel
from .models import rooms
from .models import Booking
# Create your views here.

def home_view(request):
    # member=User.objects.all()
    return render(request,'index.html')

def home_register(request):
    member=User.objects.all()
    return render(request,'registration.html',{'members': member})

def home_login(request):
    return render(request, 'login.html')

def insert(request):
    members=User(name=request.POST['name'], email=request.POST['email'], password=request.POST['password'], address=request.POST['address'])
    members.save()
    return redirect('/')