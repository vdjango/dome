from rest_framework import status
from rest_framework.test import APITestCase


class UpdateAPITestCase(APITestCase):
    """单元测试"""
    def test_get_update(self):
        response = self.client.get('/app/update/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        response = self.client.get('/app/update/', data={"uid": 2, "number": 90}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class rankingAPITestCase(APITestCase):
    """单元测试"""
    def test_get_ranking(self):
        response = self.client.get('/app/ranking/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_ranking_limt(self):
        response = self.client.get('/app/ranking/?uid=5', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

