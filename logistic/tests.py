from rest_framework.test import APITestCase


class TestAPIViews(APITestCase):
    def test_sample_view(self):
        client = APITestCase()
        response = client.get('/test/')
        self.assertEqual(response.status_code, 200)
