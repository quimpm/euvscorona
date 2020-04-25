from django.urls import path
from apps.product import views
from django.urls import reverse_lazy

urlpatterns = [
    path('<tag>/', views.NearbyProductsByTagList.as_view(), name="nearbytag"),
    path('all', reverse_lazy('nearbytag', args=['all']), name='all'),
]


