from .serializers import DataSerializer, SiteSerializer
from .models import Data, Site
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SiteList(APIView):

    def get(self, request, format=None):
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)

class SiteDetail(APIView):

    def get_object(self, pk):
        try:
            return Site.objects.get(pk=pk)
        except Site.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SiteSerializer(snippet)
        return Response(serializer.data)

