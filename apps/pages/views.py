from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from apps.users.models import CustomUser
from apps.product.models import Tag

class HomePageView(TemplateView):
    template_name = "home.html"


class PerfilView(LoginRequiredMixin, DetailView):
    template_name = "userdetail/perfil.html"
    context_object_name = 'profile'
    login_url = reverse_lazy('login')
    queryset = get_user_model().objects.all()

