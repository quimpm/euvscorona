class PerfilpageTests(SimpleTestCase):

    def test_perfilpage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_perfilpage_url_name(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_perfilpage_template(self):
        response = self.client.get('<id>/')
        self.assertTemplateUsed(response, 'perfil.html')