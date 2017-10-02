import requests
from bs4 import BeautifulSoup


def fetch_page_content(url, params=None):
    """Fetches content from given url

    Args:
        url (str): url to be fetched
        params (dict): additional query params

    Returns:
        Web page content in text format

    """
    r = requests.get(url, params=params)
    return r.text


def text_to_html(text):
    """Convert text to html

    Args:
        text (str): content to be converted

    Returns:
        Beautiful soup html object (soup)

    """
    return BeautifulSoup(text, 'html.parser')


def parse_content_by_attrobj(html, tag, attrlist):
    """Fetches inner string content from specified location

    Args:
        html (soup): html tree
        tag (str): target tag
        attrlist (dict): target tag's identifier attribute in key-val pair

    Returns:
        Content in string format

    """
    elem = html.find_all(tag, attrlist)
    return elem[0].string if len(elem) else ''


def parse_innerhtml_by_attrobj(html, tag, attrlist):
    """Fetches inner html from specified location

    Args:
        html (soup): html tree
        tag (str): target tag
        attrlist (dict): target tag's identifier attribute in key-val pair

    Returns:
        Inner html content

    """
    elem = html.find_all(tag, attrlist)
    return str(elem[0]) if len(elem) else ''


def parse_attrval_by_attrobj(html, tag, attrlist, filterkey):
    """Fetch value of given attr key from tag

    Args:
        html (soup): html tree
        tag (str): target tag
        attrlist (dict): target tag's identifier attribute in key-val pair
        filterkey (str): key of attribute whose value needs to be fetched

    Returns:
        Attribute value

    """
    elem = html.find_all(tag, attrlist)
    return elem[0].get(filterkey) if len(elem) else ''


def parse_attrlist_by_attrobj(html, tag, attrlist, filterkey):
    """Fetches values of give attr key from all matching tags

    Args:
        html (soup): html tree
        tag (str): target tag
        attrlist (dict): target tag's identifier attribute in key-val pair
        filterkey (str): key of attribute whose value needs to be fetched

    Returns:
        List of attribute values

    """
    return list(map(
        lambda x: x.get(filterkey), html.find_all(tag, attrlist)
    ))
