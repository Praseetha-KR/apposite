import datetime
from .operations import save_app, save_developer, save_screenshot, filter_apps
from .scrapers import (
    PlayStoreSearchScraper, PlayStoreAppDetailsScraper
)

RESULTS_COUNT = 10


class AppSearchProcessor:
    @staticmethod
    def __fetch_app_info(app_id):
        return PlayStoreAppDetailsScraper.get(app_id)

    @classmethod
    def query(cls, q):
        app_ids = PlayStoreSearchScraper.query(q, RESULTS_COUNT)
        return list(map(lambda x: cls.__fetch_app_info(x), app_ids))


class AppStoreProcessor:
    @staticmethod
    def __process_app_obj(app):
        developer_obj = save_developer(
            app['developer_name'], app['developer_email']
        )
        app_obj = save_app(
            app['id'],
            app['name'],
            app['desc'],
            app['icon'],
            app['rating'],
            app['review_count'],
            datetime.datetime.strptime(app['published_date'], "%d %B %Y").date(),
            app['current_version'],
            app['supported_os'],
            app['total_downloads'],
            developer_obj
        )
        save_screenshot(app['screenshots'], app_obj)
        return app_obj

    @classmethod
    def save_apps(cls, apps):
        app_ids = []
        for a in apps:
            app = cls.__process_app_obj(a)
            app_ids.append(app.id)
        return filter_apps(app_ids)
