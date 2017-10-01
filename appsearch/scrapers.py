import re
from appsearch.utils import (
    fetch_page_content, text_to_html,
    parse_content_by_attrobj, parse_innerhtml_by_attrobj,
    parse_attrval_by_attrobj, parse_attrlist_by_attrobj
)

PLAYSTORE_BASE_URL = 'https://play.google.com/store/'
SCRAPER_APPID_MAP = {
    'appid_attr': 'data-docid',
    'tag': 'div',
    'attr_key': 'class',
    'attr_val': 'card'
}
SCRAPER_APP_MAP = {
    'name': {
        'fetch': 'innertext',
        'tag': 'div',
        'attr_key': 'class',
        'attr_val': 'id-app-title'
    },
    'icon': {
        'fetch': 'attrval',
        'tag': 'img',
        'attr_key': 'class',
        'attr_val': 'cover-image',
        'filter_attr_key': 'src'
    },
    'desc': {
        'fetch': 'innerhtml',
        'tag': 'div',
        'attr_key': 'class',
        'attr_val': 'text-body'
    },
    'rating': {
        'fetch': 'innertext',
        'tag': 'div',
        'attr_key': 'class',
        'attr_val': 'score'
    },
    'reviews_count': {
        'fetch': 'innertext',
        'tag': 'span',
        'attr_key': 'class',
        'attr_val': 'reviews-num'
    },
    'published_date': {
        'fetch': 'innertext',
        'tag': 'div',
        'attr_key': 'itemprop',
        'attr_val': 'datePublished'
    },
    'current_version': {
        'fetch': 'innertext',
        'tag': 'div',
        'attr_key': 'itemprop',
        'attr_val': 'softwareVersion'
    },
    'supported_os': {
        'fetch': 'innertext',
        'tag': 'div',
        'attr_key': 'itemprop',
        'attr_val': 'operatingSystems'
    },
    'total_downloads': {
        'fetch': 'innertext',
        'tag': 'div',
        'attr_key': 'itemprop',
        'attr_val': 'numDownloads'
    },
    'screenshots': {
        'fetch': 'attrvallist',
        'tag': 'img',
        'attr_key': 'class',
        'attr_val': 'screenshot',
        'filter_attr_key': 'src'
    },
    'developer_name': {
        'fetch': 'innertext',
        'tag': 'span',
        'attr_key': 'itemprop',
        'attr_val': 'name'
    },
    'developer_email': {
        'fetch': '',
        'tag': 'a',
        'attr_key': 'class',
        'attr_val': 'dev-link',
        'filter_attr_key': 'href'
    }
}
FETCHTYPE_FN_MAP = {
    'innertext': parse_content_by_attrobj,
    'innerhtml': parse_innerhtml_by_attrobj,
    'attrval': parse_attrval_by_attrobj,
    'attrvallist': parse_attrlist_by_attrobj
}
EMAIL_REGEXP = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}'


class PlayStoreSearchScraper:
    @staticmethod
    def __query_app_ids(html, limit):
        return list(
            map(lambda x: x.div.get(
                SCRAPER_APPID_MAP['appid_attr']
            ), html.findAll(
                SCRAPER_APPID_MAP['tag'],
                {SCRAPER_APPID_MAP['attr_key']: SCRAPER_APPID_MAP['attr_val']}
            )[:limit])
        )

    @classmethod
    def query(cls, q, limit):
        content = fetch_page_content(
            PLAYSTORE_BASE_URL + 'search', {'q': q, 'c': 'apps'}
        )
        html = text_to_html(content)
        return cls.__query_app_ids(html, limit)


class PlayStoreAppDetailsScraper:
    @staticmethod
    def __get_dev_email(html):
        dev_links = parse_attrlist_by_attrobj(
            html, SCRAPER_APP_MAP['developer_email']['tag'],
            {SCRAPER_APP_MAP['developer_email'][
                'attr_key'
            ]: SCRAPER_APP_MAP['developer_email']['attr_val']},
            SCRAPER_APP_MAP['developer_email']['filter_attr_key']
        )
        filtered_emails = list(
            filter(lambda x: x, map(lambda x: re.match(
                r'mailto:' + EMAIL_REGEXP, x
            ), dev_links))
        )
        return filtered_emails[0].group()[7:] if len(filtered_emails) else ''
        # 7 is the length of 'mailto'

    @staticmethod
    def __get_parse_fn_args(html, o):
        arglist = (html, o['tag'], {o['attr_key']: o['attr_val']})
        attrFilter = o.get('filter_attr_key', None)
        if attrFilter:
            arglist += (attrFilter,)
        return arglist

    @staticmethod
    def __html_to_app_obj(doc):
        app = {}

        for k, v in SCRAPER_APP_MAP.items():
            if not v['fetch']:
                continue
            app[k] = FETCHTYPE_FN_MAP[v['fetch']].__call__(
                *PlayStoreAppDetailsScraper.__get_parse_fn_args(doc, v)
            )

        app['developer_email'] = PlayStoreAppDetailsScraper.__get_dev_email(
            doc
        )
        return app

    @classmethod
    def get(cls, id):
        content = fetch_page_content(
            PLAYSTORE_BASE_URL + 'apps/details', {'id': id}
        )
        html = text_to_html(content)
        return cls.__html_to_app_obj(html)
