from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    STATES = [
            ("AT", "Austria"),
            ("IT", "Italy"),
            ("BE", "Belgium"),
            ("LV", "Latvia"),
            ("BG", "Bulgaria"),
            ("LT", "Lithuania"),
            ("HR", "Croatia"),
            ("LU", "Luxembourg"),
            ("CY", "Cyprus"),
            ("MT", "Malta"),
            ("CZ", "Czechia"),
            ("NL", "Netherlands"),
            ("DK", "Denmark"),
            ("PL", "Poland"),
            ("EE", "Estonia"),
            ("PT", "Portugal"),
            ("FI", "Finland"),
            ("RO", "Romania"),
            ("FR", "France"),
            ("SK", "Slovakia"),
            ("DE", "Germany"),
            ("SI", "Slovenia"),
            ("GR", "Greece"),
            ("ES", "Spain"), 
            ("HU", "Hungary"),
            ("SE", "Sweden"),
            ("IE", "Ireland"),
            ]
    photo = models.ImageField(upload_to='img/user/', default=None, blank=True)
    description = models.TextField(blank=True)
    tin = models.CharField(max_length=32, unique=True, blank=True)
    country = models.CharField(max_length=2, choices=STATES, default="DE", blank=True)
    fiscal_address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

    REQUIRED_FIELDS = ['tin', 'fiscal_address', 'phone', 'lat', 'lon']


