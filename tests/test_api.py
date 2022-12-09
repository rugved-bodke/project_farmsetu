from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

# Tests for checking DB connection
# class DBConnectionTest(TestCase):
#     def test_db_connection(self):
#         response = self.client.get(reverse("db_connection"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)