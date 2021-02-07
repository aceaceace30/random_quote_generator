from django.test import TestCase
from django.urls import reverse


class MainTestCase(TestCase):

    def test_main(self):
        """Asserts that the main page is working"""
        url = reverse('main')
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
