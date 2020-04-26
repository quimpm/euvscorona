from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('profile/<int:pk>/', views.PerfilView.as_view(), name="perfil"),
        path('', views.HomePageView.as_view(), name="home"),
]
