from django.views.generic import TemplateView
from django.shortcuts import render
from .processors import SearchProcessor, StorageProcessor


class IndexView(TemplateView):
    template_name = "appsearch/index.html"


class AppsSearchView(TemplateView):
    template_name = "appsearch/search.html"

    def get(self, request):
        search_q = request.GET.get('q', None)
        tag = search_q if (search_q and len(search_q)) else 'unicorn'

        apps = []
        apps = StorageProcessor.query_cached_apps(tag)
        if not len(apps):
            search_result = SearchProcessor.query(tag)
            apps = StorageProcessor.save_apps(search_result, tag)

        return render(request, self.template_name, {'apps': apps})


class AppDetailView(TemplateView):
    template_name = "appsearch/detail.html"
