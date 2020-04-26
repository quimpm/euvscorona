from django.test import SimpleTestCase, RequestFactory, TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from apps.pages.views import PerfilView

class PerfilpageTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
                username='garga', password='testpass123', tin='12345T', lat=1, lon=1
                )
        self.user.save()
        self.client.login(username='garga', password='testpass123')
        

    def test_perfilpage_status_code(self):
        response = self.client.get('/profile/1')
        self.assertEqual(response.status_code, 200)

    def test_perfilpage_url_name(self):
        response = self.client.get(reverse('profile', args=[1]))
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_perfilpage_template(self):
        response = self.client.get('profile/1/')
        self.assertTemplateUsed(response, 'userdetail/perfil.html')


class ProfileContextTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
                    username='garga', password='testpass123', tin='12345T', lat=1, lon=1
                )
        self.user.save()
        self.factory = RequestFactory()
        self.request = self.factory.get('profile/1/)')
        self.view = PerfilView()
        self.view.setup(self.request)
        print(self.view)


    def test_context(self):
        context = self.view.get_context_data()
        self.assertIn('profiles', context)
    
