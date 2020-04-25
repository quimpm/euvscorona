from django.test import TestCase
from apps.product.models import Tag, Product
from django.contrib.auth import get_user_model


class CustomProductTest(TestCase):

    def test_simple_product(self):
        parent_tag = Tag(name='Alimentation', parent=None)
        parent_tag.save()
        son_tag = Tag(name='Potatoes', parent=parent_tag)
        son_tag.save()
        User = get_user_model()
        user = User.objects.create_user(
            username="wil",
            email="will@email.com",
            password='testpass123',
            tin='12345X',
            fiscal_address='St. Nothing',
            phone='123456789',
            lat=1.41,
            lon=1.51,
            description='Some weird description',
            country='ES',
        )
        product = Product(
            creator=user,
            tag=son_tag,
            name='Patata Manhattan',
            description='45kg bag of potatoes',
        )
        product.save()
        self.assertEquals(user, product.creator)
        self.assertEquals(son_tag, product.tag)
        self.assertEquals(parent_tag, product.tag.parent)
        self.assertEquals('Patata Manhattan', product.name)
        self.assertEquals('45kg bag of potatoes', product.description)
