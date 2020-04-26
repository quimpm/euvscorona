from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from apps.product.models import Tag, Product
import utilities.src.latlon as latlon
from django.views import generic
from .forms import ProductCreationForm
from django import http


# Create your views here.

class AddProductPageView(generic.CreateView, LoginRequiredMixin):
    form_class = ProductCreationForm
    template_name = 'addproduct.html'
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk':self.request.user.pk})

    def form_valid(self, form):
        product = form.save(commit=False)
        product.creator = self.request.user
        product.save()     
        return http.HttpResponseRedirect(self.get_success_url())
    

class NearbyProductsByTagList(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/tags.html'
    
    
    def get_queryset(self):
        def get_key(func):
            def a(product):
                return(func(product.creator))
            return a
        px = latlon.Point(self.request.user.lat, self.request.user.lon)
        tag = self.request.GET.get('q', 'all')
        try:
            tags = Tag.objects.get(name=tag)
        except Tag.DoesNotExist:
            return None
        if tags == None:
            return None
        if tag == "all":
            return sorted(Product.objects.all(), key=get_key(latlon.get_lanlonkey(px)))
        objs = Product.objects.filter(tag=tags)
        return sorted(objs, key=get_key(latlon.get_lanlonkey(px)))

