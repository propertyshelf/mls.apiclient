# -*- coding: utf-8 -*-
"""Test helpers for mls.apiclient."""

# python imports
import itertools
import os
import re
import responses
import urllib

# local imports
from mls.apiclient import (
    REST_API_URL,
    REST_API_VERSION,
)
from mls.apiclient import utils

HOST = 'demomls.com'
BASE_URL = 'http://{0}'.format(HOST)
BASE_PARAMS = {
    'apikey': 'YOUR_API_KEY',
    'lang': 'en',
}


def setup_fixtures():
    """Setup the test fixtures for integration tests."""
    # register the development endpoints
    _register(
        'developments',
        params=BASE_PARAMS,
        fixture='integration/development_list_26-1.json',
    )
    _register(
        'developments',
        params=dict(
            {
                'fields': ''.join([
                    'id,title,logo,location,lot_size,location_type,',
                    'geographic_type,number_of_listings,number_of_phases,',
                    'number_of_groups,number_of_pictures',
                ]),
                'limit': 5,
                'offset': 0,
            },
            **BASE_PARAMS),
        fixture='integration/development_list_26-1.json',
    )


def load_fixture(name, path=None):
    """Return a file-like fixture, just like urlopen would."""
    if path is None:
        path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'tests',
            'fixtures',
        )
    fixture = open(os.path.join(path, name), 'r')
    return fixture.read()


def get_url(base_url, endpoint):
    """Return the endpoint URL."""
    return '/'.join([
        base_url,
        endpoint,
    ])


def api_base_url():
    """Return the API base URL."""
    return utils.join_url(BASE_URL, REST_API_URL, REST_API_VERSION)


def _register(endpoint, content=None, path=None, fixture=None, params=None):
    if fixture:
        content = load_fixture(fixture, path=path)
    base_url = get_url(api_base_url(), endpoint)
    if not params:
        responses.add(
            responses.GET,
            re.compile(base_url),
            body=content,
            match_querystring=True,
            status=200,
            content_type='application/json',
        )
    else:
        for keys in itertools.permutations(params.keys()):
            query = urllib.urlencode(
                [(key, params.get(key)) for key in keys]
            )
            responses.add(
                responses.GET,
                re.compile('\?'.join((base_url, query))),
                body=content,
                match_querystring=True,
                status=200,
                content_type='application/json',
            )
