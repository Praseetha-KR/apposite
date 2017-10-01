from django.conf.urls import url
from appsearch.views import IndexView, AppsSearchView, AppDetailView

urlpatterns = [
    url("^search/?", AppsSearchView.as_view(), name='search'),
    url('^app/(?P<id>.+)/?', AppDetailView.as_view(), name='app_detail'),
    url('^', IndexView.as_view(), name='index'),
]
