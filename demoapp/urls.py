from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
    path('',views.index),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout)
]
