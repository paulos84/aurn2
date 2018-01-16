from .serializers import DataSerializer, SiteSerializer
from .models import Data, Site
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics


class SiteList(APIView):

    def get(self, request, format=None):
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)

class SiteDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class DataList(APIView):

    def get(self, request, format=None):
        data_list = Data.objects.all()
        serializer = DataSerializer(data_list, many=True)
        return Response(serializer.data)


class AllSiteData(APIView):

    def get_objects(self, code):
        try:
            return Data.objects.filter(site__code=code)
        except Site.DoesNotExist:
            raise Http404

    def get(self, request, site, format=None):
        site_data = self.get_object(site)
        serializer = SiteSerializer(site_data, many=True)
        return Response(serializer.data)

