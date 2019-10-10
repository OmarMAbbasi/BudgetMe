from django.urls import path
from docusign import views

urlpatterns = [
    path('', views.docusign),
]
