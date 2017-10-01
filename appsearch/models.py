from django.db import models
from taggit.managers import TaggableManager


class Developer(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)


class App(models.Model):
    appid = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    desc = models.TextField(null=True)
    icon = models.URLField()
    rating = models.FloatField()
    review_count = models.CharField(max_length=20)
    current_version = models.CharField(max_length=20)
    supported_os = models.CharField(max_length=20)
    total_downloads = models.CharField(max_length=30)
    published_date = models.DateField()
    developer = models.ForeignKey(
        'Developer', related_name='developer', null=True
    )
    tags = TaggableManager()


class Screenshot(models.Model):
    app = models.ForeignKey('App', related_name='screenshots')
    url = models.URLField()
