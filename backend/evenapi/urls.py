from django.urls import path
from evenapi import views

urlpatterns = [
    path('post/', views.evenapipost),
    path('get/', views.evenapiget),
]
