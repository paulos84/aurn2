from django.db import models
from bs4 import BeautifulSoup
import requests
from api.data.hourly import hourly_data, validate_data
from api.data.site_info import site_list, get_info


class Site(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name='Site name')
    code = models.CharField(unique=True, max_length=10, verbose_name='Site code')
    region = models.CharField(max_length=100, verbose_name='UK region', help_text='e.g. east-anglia')
    environ = models.CharField(max_length=100, verbose_name='Environment type', help_text='e.g. urban-traffic')
    url = models.URLField(max_length=1000, verbose_name='DEFRA website link', help_text='URL link to DEFRA webpage')
    map_url = models.URLField(max_length=1000, verbose_name='Google maps url')
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __repr__(self):
        return self.name

    @staticmethod
    def populate():
        for site in site_list:
            site_entry = Site.objects.create(**get_info(site))
            site_entry.save()


class Data(models.Model):
    o3 = models.CharField(max_length=10)
    no2 = models.CharField(max_length=10)
    so2 = models.CharField(max_length=10)
    pm25 = models.CharField(max_length=10)
    pm10 = models.CharField(max_length=10)
    time = models.CharField(max_length=50)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __repr__(self):
        return 'Data model for {} at {}'.format(self.site, self.time)

    hours = ', '.join([str(i) for i in range(24)])

    @staticmethod
    def update():
        page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels',
                            headers={'User-Agent': 'Not blank'}).content
        soup = BeautifulSoup(page, 'lxml')
        for site in Site.objects.all():
            data = validate_data(hourly_data(soup, site.name))
            if data:
                site_data = Data.objects.create(site=site, **data)
                site_data.save()
