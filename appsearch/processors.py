from appsearch.scrapers import (
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
