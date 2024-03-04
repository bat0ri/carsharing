from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from catalog.models import Transport, TransportCategory


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Каталог')
        self.assertTemplateUsed(response, 'catalog/catalog.html')
