from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from .views import DataViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', DataViewSet)

urlpatterns = [
    url(r'^sites/$', views.SiteList.as_view()),
    url(r'^sites/(?P<pk>[0-9]+)/$', views.SiteDetail.as_view()),
    url(r'^recent-data/(?P<code>\w+)/(?P<days>[0-9]+)/$', views.RecentSiteData.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += router.urls

