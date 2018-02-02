from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import DataSerializer, SiteSerializer
from datetime import datetime, date, timedelta
from .models import Data, Site
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


class RecentDataViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request, format=None):
        """ return data from the Data Custom Manager for latest hourly values"""
        queryset = Data.recent.all()
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)

    queryset = Data.recent.all()


class AllSiteData(APIView):

    def get(self, request, code, format=None):
        """ filter results according to the site code """
        queryset = Data.objects.filter(site__code=code)
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)


class RecentSiteData(APIView):

    def get(self, request, code, days, format=None):
        """ filter results according to the site code and number of recent days """
        queryset = Data.objects.filter(site__code=code).order_by('-id')[:int(days)*24]
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)


class DateFilterData(APIView):
    today = datetime.strftime(date.today(), "%Y-%m-%d")

    def get(self, request, date1=today, date2=today, format=None):
        """ filter results by either a date range, a single date or today """
        if date1 != self.today and date2 == self.today:
            date2 = date1
        start = datetime.strptime(date1, "%Y-%m-%d") + timedelta(days=-1)
        end = datetime.strptime(date2, "%Y-%m-%d") + timedelta(days=1)
        queryset = Data.objects.filter(time__gt=start, time__lt=end)
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)


class SiteViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Site.objects.all()
    serializer_class = SiteSerializer


def order_pie(request):
    """ This returns in a few seconds """

    Data.update()
    return 'you ordered pie?'
