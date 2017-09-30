import re
from appsearch.utils import (
    fetch_page_content, text_to_html, get_innerhtml_by_attr,
    get_content_by_attr, get_attr_by_class, query_attr_arr_by_class
)

PLAYSTORE_BASE_URL = 'https://play.google.com/store/'


class PlayStoreAppDetailsScraper:
    def __init__(self, id):
        self.id = id
        self.app = {}

    def _get_developer_email(self, html):
        dev_links = query_attr_arr_by_class(html, 'a', 'dev-link', 'href')
        filtered_email = list(
            filter(lambda x: x, map(lambda x: re.match(
                r'mailto:[a-zA-Z0-9\._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}', x
            ), dev_links))
        )
        return filtered_email[0].group()[7:] if filtered_email else ''

    def _app_html_to_obj(self, html):
        app = {}
        app['icon'] = get_attr_by_class(
            html, 'img', 'cover-image', 'src'
        )
        app['name'] = get_content_by_attr(
            html, 'div', {'class': 'id-app-title'}
        )
        app['desc'] = str(get_innerhtml_by_attr(
            html, 'div', {'class': 'text-body'}
        ))
        app['rating'] = get_content_by_attr(
            html, 'div', {'class': 'score'}
        )
        app['reviews_count'] = get_content_by_attr(
            html, 'span', {'class': 'reviews-num'}
        )
        app['published_on'] = get_content_by_attr(
            html, 'div', {'itemprop': 'datePublished'}
        )
        app['current_version'] = get_content_by_attr(
            html, 'div', {'itemprop': 'softwareVersion'}
        )
        app['supported_versions'] = get_content_by_attr(
            html, 'div', {'itemprop': 'operatingSystems'}
        )
        app['developer_email'] = self._get_developer_email(html)
        app['screenshots'] = query_attr_arr_by_class(
            html, 'img', 'screenshot', 'src'
        )
        return app

    def get(self):
        content = fetch_page_content(
            PLAYSTORE_BASE_URL + 'apps/details', {'id': self.id}
        )
        html = text_to_html(content)
        self.app = self._app_html_to_obj(html)
        return self.app


class PlayStoreSearchScraper:
    def __init__(self, q):
        self.q = q
        self.app_ids = []

    def _get_app_ids(self, html, limit):
        return list(
            map(lambda x: x.div.get('data-docid'), html.findAll(
                "div", {"class": 'card'}
            )[:limit])
        )

    def query(self, limit):
        content = fetch_page_content(
            PLAYSTORE_BASE_URL + 'search', {'q': self.q, 'c': 'apps'}
        )
        html = text_to_html(content)
        self.app_ids = self._get_app_ids(html, limit)
        return self.app_ids
