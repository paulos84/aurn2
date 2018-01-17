from .serializers import DataSerializer, SiteSerializer
from .models import Data, Site
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework import viewsets


class DataViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Data.objects.all()
    serializer_class = DataSerializer


class AllSiteData(APIView):

    def get(self, request, code, format=None):
        queryset = Data.objects.filter(site__code=code)
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)


class RecentSiteData(APIView):

    def get(self, request, code, days, format=None):
        # filter by site code and limit to the last 2 objects
        queryset = Data.objects.filter(site__code=code).order_by('-id')[:int(days)*24]
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)


class SiteList(APIView):
    def get(self, request, format=None):
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)


class SiteDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

