from django.urls import path
from . import views

urlpatterns = [
    path('', home_view, name='index'),
    path('',home_register, name='index'),
    path('', home_login, name='index'),


    ]
