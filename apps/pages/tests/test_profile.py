from django.test import SimpleTestCase, RequestFactory, TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from apps.pages.views import PerfilView

class PerfilpageTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username='garga', password='testpass123', tin='12345T', lat=1, lon=1, email='gar@ga.com'
                )
        self.user.save()
        self.client.login(username=self.user.username, password='testpass123')
        

    def test_perfilpage_status_code(self):
        response = self.client.get(f'/profile/{ self.user.pk }/')
        self.assertEqual(response.status_code, 200)

    def test_perfilpage_url_name(self):
        response = self.client.get(reverse('profile', kwargs={'pk':self.user.pk}))
        self.assertEqual(response.status_code, 200)

    def test_perfilpage_template(self):
        response = self.client.get(f'/profile/{ self.user.pk }/')
        self.assertTemplateUsed(response, 'userdetail/perfil.html')


class ProfileContextTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
                    username='garga', password='testpass123', tin='12345T', lat=1, lon=1
                )
        self.user.save()
        self.client.login(username='garga', password='testpass123')
        self.request = self.client.get(reverse('profile', kwargs={'pk':self.user.pk}))


    def test_context(self):
        self.assertIn('profile', self.request.context)
        self.assertIn('products', self.request.context)
    
