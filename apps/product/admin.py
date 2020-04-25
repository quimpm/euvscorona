from django.contrib import admin
from apps.product.models import Product, Tag

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("tag", "name",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
