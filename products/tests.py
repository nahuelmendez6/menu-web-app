from unicodedata import category

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from products.models import Category, Product
# Create your tests here.

class ProductsAPITestCase(APITestCase):
    def setUp(self):
        # Crear datos iniciales para la prueba
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.category = Category.objects.create(
            category_name="Gaseosas",
            category_description="Todas las gaseosas",
            local_owner=self.user,
        )
        self.product = Product.objects.create(
            product_name="Sprite",
            product_price=1000,
            category=self.category,
            local_owner=self.user,
            product_description="Gaseosa lima-limon",
        )

        def test_get_products(self):
            # Realiza solicitud GET
            response = self.client.get('/manage/menu/v1/products')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_post_product(self):
            # Autentica al usuario
            self.client.force_authenticate(user=self.user)

            # Datos para crear nuevo producto
            data = {
                "product_name": "Pepsi",
                "product_price": 900,
                "product_description": "Bebida gaseosa alternativa",
                "category": self.category.id,
                "local_owner": self.user.id,
            }
            response = self.client.post('/manage/menu/v1/products', data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data['product_name'], "Pepsi")

        def test_put_product(self):
            # Autentica al usuario
            self.client.force_authenticate(user=self.user)

            # Datos actualizados del producto
            data = {
                "product_name": "Coca Cola Light",
                "product_price": 1100,
                "product_description": "Bebida gaseosa baja en azúcar",
                "category": self.category.id,
                "local_owner": self.user.id,
            }
            response = self.client.put(f'/api/products/{self.product.id}/', data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['product_name'], "Coca Cola Light")

        def test_delete_product(self):
            # Autentica al usuario
            self.client.force_authenticate(user=self.user)

            # Solicitud DELETE
            response = self.client.delete(f'/api/products/{self.product.id}/')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertFalse(Products.objects.filter(id=self.product.id).exists())