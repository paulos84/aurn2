from .serializers import DataSerializer, SiteSerializer
from .models import Data, Site
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


class SiteList(APIView):

    def get(self, request, format=None):
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)


class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.retrieve(request, pk=pk)

    def delete(self, request, pk):
        return self.retrieve(request, pk=pk)


class DataList(APIView):

    def get(self, request, format=None):
        queryset = Data.objects.all()
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)


class AllSiteData(APIView):

    def get(self, request, code, format=None):
        queryset = Data.objects.filter(site__code=code)
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)
