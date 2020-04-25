from django.test import TestCase
from apps.product.models import Tag

class CustomTagTest(TestCase):

    def test_create_super_tag(self):
        parent_tag = Tag.objects.create(name='Alimentation', parent=None)
        son_tag = Tag.objects.create(name='Potatoes', parent=parent_tag)
        self.assertEquals(parent_tag, son_tag.parent)

    def test_create_simple_Tag(self):
        tag_name = 'Alimentation'
        tag = Tag.objects.create(name=tag_name, parent=None)
        self.assertEquals(tag.name, tag_name)
        self.assertIsNone(tag.parent)