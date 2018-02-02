from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from api.models import Data, Site
from api.views import AllSiteData

client = APIClient()
factory = APIRequestFactory()


class DataApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        site_dict = {"name": "Aberdeen", "code": "ABD", "region": "north-east-scotland", "environ": "urban-background",
                     "url": "https://uk-air.defra.gov.uk/networks/site-info?site_id=ABD",
                     "map_url": "https://maps.google.co.uk/?q=57.157360,-2.094278", "latitude": "57.157360",
                     "longitude": "-2.094278"}
        site = Site.objects.create(**site_dict)
        Data.objects.create(o3="10", no2="50", so2="7", pm25="15", pm10="20", time="22/01/2018 03:00", site=site)
        Data.objects.create(o3="12", no2="54", so2="7", pm25="15", pm10="20", time="22/01/2018 04:00", site=site)
        Data.objects.create(o3="12", no2="61", so2="7", pm25="14", pm10="19", time="22/01/2018 05:00", site=site)

    def test_object_name_correct(self):
        time_point = Data.objects.get(id=1)
        expected_object_name = 'Data model for {} at {}'.format(time_point.site, time_point.time)
        self.assertEquals(expected_object_name, repr(time_point))

    def test_time_max_length(self):
        time_point = Data.objects.get(id=1)
        max_length = time_point._meta.get_field('time').max_length
        self.assertEquals(max_length, 50)

    def test_url_exists(self):
        resp = self.client.get('/site-data/MY1/5/')
        self.assertEqual(resp.status_code, 200)

    def test_response(self):
        resp = self.client.get('/data/3/')
        expected_output = {'so2': '7', 'no2': '61', 'pm25': '14', 'o3': '12', 'pm10': '19', 'time': '22/01/2018 05:00',
                           'site_code': 'ABD'}
        self.assertEqual(resp.data, expected_output)

    def test_AllSiteData_view(self):
        view = AllSiteData.as_view()
        request = factory.get('/data/ABD')
        resp = view(request, code='ABD')
        resp.render()
        print(resp.content.decode(), [a for a in Data.objects.values()])
