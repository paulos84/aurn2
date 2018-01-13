from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100, verbose_name='Site name')
    code = models.CharField(max_length=10, verbose_name='Site code')
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


class Data(models.Model):
    o3 = models.CharField(max_length=10)
    no2 = models.CharField(max_length=10)
    so2 = models.CharField(max_length=10)
    pm25 = models.CharField(max_length=10)
    pm10 = models.CharField(max_length=10)
    time = models.CharField(max_length=50)
    site = models.ForeignKey(Site)

    def __repr__(self):
        return 'Data model for {} at {}'.format(self.site, self.time)