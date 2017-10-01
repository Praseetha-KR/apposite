from django.views.generic import TemplateView
from django.shortcuts import render
from appsearch.processors import AppSearchProcessor


class IndexView(TemplateView):
    template_name = "appsearch/index.html"


class AppsSearchView(TemplateView):
    template_name = "appsearch/search.html"

    def get(self, request):
        app_search = AppSearchProcessor('photo edit')
        apps = app_search.query()
        return render(request, self.template_name, {'apps': apps})


class AppDetailView(TemplateView):
    template_name = "appsearch/detail.html"
