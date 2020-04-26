from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from apps.users.models import CustomUser

class HomePageView(TemplateView):
    template_name = "home.html"


class PerfilView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "userdetail/perfil.html"
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        perfil = self.model.objects.get(pk=self.request.user.pk)
        context['perfil'] = perfil
        return context


