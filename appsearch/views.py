from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "appsearch/index.html"


class AppsSearchView(TemplateView):
    template_name = "appsearch/apps_search.html"


class AppDetailView(TemplateView):
    template_name = "appsearch/app_detail.html"
