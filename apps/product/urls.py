from django.urls import path
from apps.product import views
from django.urls import reverse_lazy

urlpatterns = [
    #path('all/', views.TagAllList.as_view(), name='all'),
    path('search/', views.NearbyProductsByTagList.as_view(), name="nearbytag"),
]


