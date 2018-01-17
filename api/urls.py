from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from .views import DataViewSet, SiteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'data', DataViewSet)
router.register(r'sites', SiteViewSet)

urlpatterns = [
    url(r'^site-data/(?P<code>\w+)/$', views.AllSiteData.as_view()),
    url(r'^site-data/(?P<code>\w+)/(?P<days>[0-9]+)/$', views.RecentSiteData.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += router.urls

