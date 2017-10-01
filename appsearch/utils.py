import requests
from bs4 import BeautifulSoup


def fetch_page_content(url, payload):
    r = requests.get(url, params=payload)
    return r.text


def text_to_html(text):
    return BeautifulSoup(text, 'html.parser')


def parse_content_by_attrobj(html, tag, attrlist):
    elem = html.find_all(tag, attrlist)
    return elem[0].string if len(elem) else ''


def parse_innerhtml_by_attrobj(html, tag, attrlist):
    elem = html.find_all(tag, attrlist)
    return str(elem[0]) if len(elem) else ''


def parse_attrval_by_attrobj(html, tag, attrlist, filterkey):
    elem = html.find_all(tag, attrlist)
    return elem[0].get(filterkey) if len(elem) else ''


def parse_attrlist_by_attrobj(html, tag, attrlist, filterkey):
    return list(map(
        lambda x: x.get(filterkey), html.find_all(tag, attrlist)
    ))
