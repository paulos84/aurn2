from rest_framework import serializers
from .models import Data, Site


#In the same way that Django provides both Form classes and ModelForm classes,
# REST framework includes both Serializer classes, and ModelSerializer classes.
class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        # fields = ('name', 'region') - specify certain
        fields = '__all__'  #sends user all field


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        # fields = ('name', 'region') - specify certain
        fields = '__all__'  #sends user all field

