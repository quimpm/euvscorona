from django.test import TestCase
from apps.product.models import Tag

class CustomTagTest(TestCase):

    def test_create_super_tag(self):
        parent_tag = Tag(name='Alimentation', parent=None)
        parent_tag.save()
        son_tag = Tag(name='Potatoes', parent=parent_tag)
        son_tag.save()
        self.assertEquals(parent_tag, son_tag.parent)

    def test_create_simple_Tag(self):
        tag_name = 'Alimentation'
        tag = Tag(name=tag_name, parent=None)
        tag.save()
        self.assertEquals(tag.name, tag_name)
        self.assertIsNone(tag.parent)
