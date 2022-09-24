from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='inicio' ),
    path('signup/',views.signup, name='signup' ),
]
