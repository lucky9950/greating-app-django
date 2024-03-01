from django.contrib import admin
from django.urls import path
from greateapp import views

urlpatterns = [
    
    path('',views.get_greeting),
]
