from django.contrib import admin
from .models import App, Developer, Screenshot


class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'appid', 'tag_list', 'developer_email')

    def tag_list(self, obj):
        return ", ".join(o.slug for o in obj.tags.all())

    def developer_email(self, obj):
        return obj.developer.email


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'email')


class ScreenshotAdmin(admin.ModelAdmin):
    list_display = ('url', 'id', 'app_name')

    def app_name(self, obj):
        return obj.app.name


admin.site.register(App, AppAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Screenshot, ScreenshotAdmin)
