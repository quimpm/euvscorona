from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from apps.product.models import Tag, Product
import utilities.src.latlon as latlon

# Create your views here.
class NearbyProductsByTagList(LoginRequiredMixin, ListView):
    template_name = 'product/tags.html'
    context_object_name = 'products'
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.kwargs['tag'])
        objs = Product.objects.filter(tag=tag)
        px = latlon.Point(self.kwargs['user'].lat, self.kwargs['user'].lon)
        return sorted(objs, key=latlon.get_lanlonkey(px))
        
