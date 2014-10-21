# -*- coding: utf-8 -*-

# python imports
import urlparse
import re

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


def join_url(url, *paths):
    """
    Joins individual URL strings together, and returns a single string.

    Usage::

        >>> utils.join_url("example.com", "index.html")
        'example.com/index.html'
    """
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url


def join_url_params(url, params):
    """Constructs percent-encoded query string from given params dictionary
     and appends to given url

    Usage::

        >>> utils.join_url_params("example.com/index.html", {"count": 5, "type": "rl"})
        example.com/index.html?count=5&type=rl
    """
    return url + '?' + urlencode(params)


def merge_dict(data, *override):
    """
    Merges any number of dictionaries together, and returns a single dictionary

    Usage::

        >>> utils.merge_dict ({"foo": "bar"}, {1: 2}, {"count": 5})
        {1: 2, 'foo': 'bar', 'count': 5}
    """
    result = {}
    for current_dict in (data,) + override:
        result.update(current_dict)
    return result


def get_link(links, name):
    """Returns a specific link from a list of links with the given format:

    links = [
        {
            "href" : "http://demomls.com",
            "rel" : "self",
        },
        {
            "href" : "http://demomls.com/next",
            "rel" : "next",
        },
    ]

    Usage::

        >>> utils.get_link(links, 'self')
        http://demomls.com
        >>> utils.get_link(links, 'next')
        http://demomls.com/next
    """
    if links is None:
        return None
    for link in links:
        if link.get('rel') == name:
            return link.get('href')


def split_url_params(url):
    """Split a url with parameters to return a tuple of the base url and a
    dictionary of the parameters.

    Usage::

        >>> utils.split_url_params('http://demomls.com?param1=value1&param2=value2')
        ('http://demomls.com', {'param1': 'value1', 'param2': 'value2'})
    """
    params = {}
    parsed = url.split('?')
    base_url = parsed[0]
    if len(parsed) > 0:
        result = urlparse.urlparse(url)
        params = dict(urlparse.parse_qsl(result.query))
    return (base_url, params)
