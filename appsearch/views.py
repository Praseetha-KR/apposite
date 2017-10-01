from django.views.generic import TemplateView
from django.shortcuts import render
from .processors import AppSearchProcessor, AppStoreProcessor


class IndexView(TemplateView):
    template_name = "appsearch/index.html"


class AppsSearchView(TemplateView):
    template_name = "appsearch/search.html"

    def get(self, request):
        query = request.GET.get('q')
        apps = AppSearchProcessor.query(query)
        cached_apps = AppStoreProcessor.save_apps(apps)
        return render(request, self.template_name, {'apps': cached_apps})


class AppDetailView(TemplateView):
    template_name = "appsearch/detail.html"
