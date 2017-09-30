from django.conf.urls import url
from appsearch.views import IndexView, AppsSearchView, AppDetailView

urlpatterns = [
    url("^search/?", AppsSearchView.as_view(), name='search'),
    url('^app/?', AppDetailView.as_view(), name='detail'),
    url('^', IndexView.as_view(), name='index'),
]
