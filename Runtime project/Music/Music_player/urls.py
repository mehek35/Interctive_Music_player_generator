
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path("", views.MUSIC),
    path("blur.html/", views.MUSIC),
    path("home/", views.home),
    path("sig.html/", views.sig),
    path("log.html/", views.log),
    
]
