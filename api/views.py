from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import DataSerializer, SiteSerializer
from datetime import datetime, date, timedelta
from .models import Data, Site


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


class DateData(APIView):

    def get(self, request, date=datetime.strftime(date.today(), "%Y-%m-%d"), format=None):
        """ filter results according to a specified day with format YYYY-MM-DD """
        dt_day = datetime.strptime(date, "%Y-%m-%d")
        start = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=-1)
        end = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)
        queryset = Data.objects.filter(time__lt=end, time__gt=start)
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)


class DateRangeData(APIView):

    def get(self, request, date1, date2, format=None):
        """ filter results according to a specified date range withs formats YYYY-MM-DD """
        uk_date1 = '{}/{}/{}'.format(*date1.split('-')[::-1])
        uk_date2 = '{}/{}/{}'.format(*date2.split('-')[::-1])
        pass


class SiteViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Site.objects.all()
    serializer_class = SiteSerializer


def order_pie(request):
    """ This returns in a few seconds """

    Data.update()
    return 'you ordered pie?'
