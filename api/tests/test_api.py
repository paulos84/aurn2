from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from api.serializers import DataSerializer
from api.models import Data

client = Client()


class GetDataTest(TestCase):

    def setUp(self):
        Data.objects.create(o3="10", no2="50", so2="7", pm25="15", pm10="20", time="22/01/2018 03:00", site_code="MY1")
        Data.objects.create(o3="12", no2="54", so2="7", pm25="15", pm10="20", time="22/01/2018 04:00", site_code="MY1")
        Data.objects.create(o3="12", no2="61", so2="7", pm25="14", pm10="19", time="22/01/2018 05:00", site_code="MY1")

    def test_url_exists(self):
        resp = self.client.get('/site-data/MY1/5/')
        self.assertEqual(resp.status_code, 200)

    def test_create(self):
        response = self.client.get('/mission/create/{0}/'.format(self.userName))
        self.assertEqual(response.status_code, 200)