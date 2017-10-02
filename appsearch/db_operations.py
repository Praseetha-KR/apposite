from .models import App, Developer, Screenshot


def save_developer(name, email):
    developer, created = Developer.objects.get_or_create(email=email)
    developer.name = name
    developer.save()

    return developer


def save_app(appid, name, desc, icon, rating, review_count, published_date,
             current_version, supported_os, total_downloads, developer):
    app, created = App.objects.get_or_create(appid=appid)
    app.name = name
    app.desc = desc
    app.icon = icon
    app.rating = rating
    app.review_count = review_count
    app.published_date = published_date
    app.current_version = current_version
    app.supported_os = supported_os
    app.total_downloads = total_downloads
    app.developer = developer
    app.save()
    return app


def save_screenshot(screenshots, app):
    screenshot_list = []
    for url in screenshots:
        screenshot, created = Screenshot.objects.get_or_create(app=app)
        screenshot.url = url
        screenshot.save()

        screenshot_list.append(screenshot)
    return screenshot_list


def save_app_tag(app, tag):
    app.tags.add(tag)
    return app.tags.all()


def filter_tagged_apps(tag):
    return App.objects.filter(tags__name__in=[tag])


def filter_apps_by_ids(app_ids):
    return App.objects.filter(id__in=app_ids)


def get_app(id):
    return App.objects.get(id=id)
