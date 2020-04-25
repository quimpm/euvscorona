from django.test import TestCase
from apps.product.models import Tag

class CustomTagTest(TestCase):

    def test_create_super_tag(self):
        parent_tag = Tag.objects.create(name='Alimentació', parent=None)
        son_tag = Tag.objects.create(name='Patates', parent=parent_tag)
        self.assertEquals(parent_tag, son_tag.parent)

    def test_create_simple_Tag(self):
        tag = Tag.objects.create(name='Alimentació', parent=None)
        self.assertEquals(tag.name, 'Alimentació')
        self.assertIsNone(tag.parent)