from django.test import TestCase
from apps.product.models import Tag, Product

class CustomProductTest(TestCase):

    def test_simple_product(self):
