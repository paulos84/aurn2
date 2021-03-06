from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from api import views
from .views import SiteViewSet, RecentDataViewSet

router = DefaultRouter()
router.register(r'current-data', RecentDataViewSet, base_name='current')
router.register(r'sites', SiteViewSet)

urlpatterns = [
    url(r'^site-data/(?P<code>\w+)/$', views.AllSiteData.as_view()),
    url(r'^site-data/(?P<code>\w+)/(?P<days>[0-9]+)/$', views.RecentSiteData.as_view()),
    url(r'^data/$', views.DateFilterData.as_view()),
    url(r'^data/(?P<date1>\d{4}-\d{2}-\d{2})/$', views.DateFilterData.as_view()),
    url(r'^data/(?P<date1>\d{4}-\d{2}-\d{2})/(?P<date2>\d{4}-\d{2}-\d{2})/$', views.DateFilterData.as_view()),
    url(r'^order-pie$', views.order_pie),
    url(r'^docs/$', views.schema_view)
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += router.urls


