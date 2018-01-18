from rest_framework import serializers
from .models import Data, Site


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    site_code = serializers.CharField(source='site.code')

    class Meta:
        model = Data
        fields = ('o3', 'no2', 'so2', 'pm25', 'pm10', 'time', 'site_code')
