from apps.product.models import Tag, Product
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="Creates @all tag"

    def handle(self, *args, **kwargs):
        pr = Product.objects.create(name='all')
        pr = Product.objects.create(name='farming')
        pr = Product.objects.create(name='metallurgy')
        pr.save()
