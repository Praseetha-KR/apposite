from django.views.generic import TemplateView
from django.shortcuts import render
from appsearch.processors import AppSearchProcessor


class IndexView(TemplateView):
    template_name = "appsearch/index.html"


class AppsSearchView(TemplateView):
    template_name = "appsearch/search.html"

    def get(self, request):
        apps = AppSearchProcessor.query('photo edit')
        return render(request, self.template_name, {'apps': apps})


class AppDetailView(TemplateView):
    template_name = "appsearch/detail.html"
