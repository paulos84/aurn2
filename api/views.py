from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import DataSerializer, SiteSerializer
import datetime
from .models import Data, Site


class DataViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Data.objects.all()
    serializer_class = DataSerializer


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


class LatestHour(APIView):

    def get(self, request, format=None):
        """ filter results according to the most recent hourly values for each site """
        queryset = Data.recent.all()
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)


class DateData(APIView):

    def get(self, request, date, format=None):
        """ filter results according to a specified day with format YYYY-MM-DD """
        uk_date = '{}/{}/{}'.format(*date.split('-')[::-1])
        queryset = Data.objects.filter(time__contains=uk_date)
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
    """ This returns in a few seconds! """


    Data.update()
    return 'you ordered pie?'