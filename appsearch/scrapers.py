import re
from appsearch.utils import (
    fetch_page_content, text_to_html, get_innerhtml_by_attr,
    get_content_by_attr, get_attr_by_class, query_attr_arr_by_class
)

PLAYSTORE_BASE_URL = 'https://play.google.com/store/'


class PlayStoreAppDetailsScraper:
    EMAIL_REGEXP = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}'

    @staticmethod
    def __get_dev_email(html):
        dev_links = query_attr_arr_by_class(html, 'a', 'dev-link', 'href')
        filtered_email = list(
            filter(lambda x: x, map(lambda x: re.match(
                r'mailto:' + PlayStoreAppDetailsScraper.EMAIL_REGEXP, x
            ), dev_links))
        )
        return filtered_email[0].group()[7:] if filtered_email else ''
        # 7 is len of prefix 'mailto'

    @staticmethod
    def __html_to_app_obj(html):
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
        app['developer_email'] = PlayStoreAppDetailsScraper.__get_dev_email(
            html
        )
        app['screenshots'] = query_attr_arr_by_class(
            html, 'img', 'screenshot', 'src'
        )
        return app

    @classmethod
    def get(cls, id):
        content = fetch_page_content(
            PLAYSTORE_BASE_URL + 'apps/details', {'id': id}
        )
        html = text_to_html(content)
        return cls.__html_to_app_obj(html)


class PlayStoreSearchScraper:
    @staticmethod
    def __query_app_ids(html, limit):
        return list(
            map(lambda x: x.div.get('data-docid'), html.findAll(
                "div", {"class": 'card'}
            )[:limit])
        )

    @classmethod
    def query(cls, q, limit):
        content = fetch_page_content(
            PLAYSTORE_BASE_URL + 'search', {'q': q, 'c': 'apps'}
        )
        html = text_to_html(content)
        return cls.__query_app_ids(html, limit)
