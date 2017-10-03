from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .processors import SearchProcessor, StorageProcessor


class IndexView(TemplateView):
    template_name = "appsearch/index.html"


class AppsSearchView(TemplateView):
    template_name = "appsearch/search.html"

    def get(self, request):
        search_q = request.GET.get('q', '')
        tag = search_q.lower() if (search_q and len(search_q)) else 'unicorn'
        apps = StorageProcessor.query_cached_apps(tag)
        if not len(apps):
            search_result = SearchProcessor.query(tag)
            apps = StorageProcessor.save_apps(search_result, tag)
        return render(request, self.template_name, {
            'apps': apps, 'q': search_q
        })

    def post(self, request):
        return HttpResponseRedirect('/search?q=' + request.POST.get('q', None))


class AppDetailView(TemplateView):
    template_name = "appsearch/detail.html"

    def get(self, request, id):
        app = StorageProcessor.fetch_app(id)
        return render(request, self.template_name, {'app': app})
