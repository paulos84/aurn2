from django.test import TestCase
from api.models import Data, Site


class DataModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        site_dict = {"name": "Aberdeen", "code": "ABD", "region": "north-east-scotland", "environ": "urban-background",
                     "url": "https://uk-air.defra.gov.uk/networks/site-info?site_id=ABD",
                     "map_url": "https://maps.google.co.uk/?q=57.157360,-2.094278", "latitude": "57.157360",
                     "longitude": "-2.094278"}
        data_dict = {"o3": "11", "no2": "99", "so2": "16", "pm25": "13", "pm10": "18", "time": "22/01/2018 09:00"}
        site = Site.objects.create(**site_dict)
        Data.objects.create(**data_dict, site=site)

    def test_object_name_correct(self):
        time_point = Data.objects.get(id=1)
        expected_object_name = 'Data model for {} at {}'.format(time_point.site, time_point.time)
        self.assertEquals(expected_object_name, repr(time_point))

    def test_time_max_length(self):
        time_point = Data.objects.get(id=1)
        max_length = time_point._meta.get_field('time').max_length
        self.assertEquals(max_length, 50)
