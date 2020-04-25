from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.SignupPageView.as_view(), name="signup"),
]