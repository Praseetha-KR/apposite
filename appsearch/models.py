from django.db import models
from taggit.managers import TaggableManager


class Developer(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(default='admin@localhost')


class App(models.Model):
    appid = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=True)
    desc = models.TextField(null=True)
    icon = models.URLField(null=True)
    rating = models.FloatField(default=0.0)
    review_count = models.CharField(max_length=20, null=True)
    current_version = models.CharField(max_length=20, null=True)
    supported_os = models.CharField(max_length=255, null=True)
    total_downloads = models.CharField(max_length=255, null=True)
    published_date = models.DateField(auto_now=True)
    developer = models.ForeignKey(
        'Developer', related_name='developer', null=True
    )
    tags = TaggableManager()


class Screenshot(models.Model):
    app = models.ForeignKey('App', related_name='screenshots')
    url = models.URLField(null=True)
