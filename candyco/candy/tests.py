from django.test import TestCase, Client

class IndexTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.client.get('/candy/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello World", str(response.content))
