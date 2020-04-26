from django.test import SimpleTestCase
from django.urls import reverse, resolve


class PerfilpageTests(SimpleTestCase):

    def test_perfilpage_status_code(self):
        response = self.client.get('/profile/<id>')
        self.assertEqual(response.status_code, 200)

    def test_perfilpage_url_name(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_perfilpage_template(self):
        response = self.client.get('profile/<id>/')
        self.assertTemplateUsed(response, 'userdetail/perfil.html')