from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from userinfo import views

urlpatterns = [
    path('userinfo/', views.userinfo_list),
    path('userinfo/<int:pk>/', views.userinfo_detail),
    path('microloan/', views.microloan_list),
    path('microloan/<int:pk>/', views.microloan_detail),
]
