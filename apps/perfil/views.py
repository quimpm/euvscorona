from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from apps.users.models import CustomUser


class PerfilView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "perfil.html"
    login_url = reverse_lazy('login')

