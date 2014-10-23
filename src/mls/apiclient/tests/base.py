# -*- coding: utf-8 -*-
"""Test case base class."""

# python imports
import httpretty
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# local imports
from mls.apiclient import (
    REST_API_URL,
    REST_API_VERSION,
)
from mls.apiclient.tests import utils


class BaseTestCase(unittest.TestCase):
    """Test case base class."""
    HOST = 'demomls.com'
    PATH = '/api'

    @property
    def BASE_URL(self):
        """Return the MLS base url used for the tests."""
        return 'http://{0}'.format(self.HOST)

    @property
    def URL(self):
        """Return the MLS API endpoint url for the tests."""
        return self.BASE_URL + self.PATH

    def setup_integration_test(self):
        """Setup all URL mocks to run a full integration test."""
        API_BASE = '/'.join((self.BASE_URL, REST_API_URL, REST_API_VERSION))

        def _register(endpoint, content=None, fixture=None):
            if fixture:
                content = utils.load_fixture(fixture)
            httpretty.register_uri(
                httpretty.GET,
                utils.get_url(API_BASE, endpoint),
                body=content,
            )

        _register('developments', fixture='development_list_0.json')
