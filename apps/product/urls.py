from django.urls import path
from apps.product import views

urlpatterns = [
    path('<tag>/', views.NearbyProductsByTagList.as_view(), "nearbytag")
]


