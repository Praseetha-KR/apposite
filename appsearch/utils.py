import requests
from bs4 import BeautifulSoup


def fetch_page_content(url, payload):
    r = requests.get(url, params=payload)
    return r.text


def text_to_html(text):
    return BeautifulSoup(text, 'html.parser')


def get_content_by_attr(html, tag, attr):
    elem = html.find_all(tag, attr)
    return elem[0].string if elem else ''


def get_innerhtml_by_attr(html, tag, attr):
    elem = html.find_all(tag, attr)
    return elem[0] if elem else ''


def get_attr_by_class(html, tag, classname, attr):
    elem = html.find_all(tag, {'class': classname})
    return elem[0].get(attr) if elem else ''


def query_attr_arr_by_class(html, tag, classname, attr):
    return list(map(
        lambda x: x.get(attr), html.find_all(tag, {'class': classname})
    ))
