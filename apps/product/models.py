from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)
    parent = models.ForeignKey("Tag", on_delete=models.CASCADE, null=True)


class Product(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    name = models.CharField(max_length=78)
    description = models.TextField()
    photo = models.ImageField(upload_to='img/product/', default=None, blank=True)


