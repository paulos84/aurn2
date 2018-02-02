from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from api import views
from .views import SiteViewSet, RecentDataViewSet

router = DefaultRouter()
router.register(r'current', RecentDataViewSet, base_name='current')
router.register(r'sites', SiteViewSet)

urlpatterns = [
    url(r'^site-data/(?P<code>\w+)/$', views.AllSiteData.as_view()),
    url(r'^site-data/(?P<code>\w+)/(?P<days>[0-9]+)/$', views.RecentSiteData.as_view()),
    url(r'^data/(?P<date>\d{4}-\d{2}-\d{2})/$', views.DateData.as_view()),
    #url(r'^recent-data/$', views.LatestHour.as_view()),
    url(r'^order-pie$', views.order_pie)
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += router.urls



    #url(r'^data/(?P<date>\d{4}-\d{2}-\d{2})/$', views.DateData.as_view()),
    #url(r'^data/(?P<date1>\w+)/(?P<date2>[0-9]+)/$', views.DateRangeData.as_view()),
   #url(r'^order-pie$', views.order_pie)


