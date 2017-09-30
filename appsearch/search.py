from appsearch.scrapers import (
    PlayStoreSearchScraper, PlayStoreAppDetailsScraper
)

RESULTS_COUNT = 10


class PlayStoreAppsSearch:
    def __init__(self, q):
        self.q = q
        self.apps = []

    def _fetch_app_details(self, app_id):
        appDetailScraper = PlayStoreAppDetailsScraper(app_id)
        return appDetailScraper.get()

    def query(self):
        searchScraper = PlayStoreSearchScraper(self.q)
        app_ids = searchScraper.query(RESULTS_COUNT)
        self.apps = list(map(lambda x: self._fetch_app_details(x), app_ids))
        return self.apps
