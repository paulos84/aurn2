from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import DataSerializer, SiteSerializer
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


class SiteViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Site.objects.all()
    serializer_class = SiteSerializer


def order_pie(request):
    """ This returns in a few seconds! """


    Data.update()
    return 'you ordered pie?'