from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from apps.product.models import Tag, Product
import utilities.src.latlon as latlon

# Create your views here.
class NearbyProductsByTagList(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/tags.html'
    
    
    def get_queryset(self):
        tag = self.request.GET.get('q', 'all')
        tags = Tag.objects.get(name=tag)
        objs = Product.objects.filter(tag=tags)
        px = latlon.Point(self.request.user.lat, self.request.user.lon)
        return sorted(objs, key=latlon.get_lanlonkey(px))



