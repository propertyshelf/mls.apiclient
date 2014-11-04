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
from mls.apiclient.utils import join_url


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

    @property
    def API_BASE(self):
        """Return the base API url for the tests."""
        return join_url(self.BASE_URL, REST_API_URL, REST_API_VERSION)

    def setup_integration_test(self):
        """Setup all URL mocks to run a full integration test."""

        def _register(endpoint, content=None, fixture=None):
            if fixture:
                content = utils.load_fixture(fixture)
            httpretty.register_uri(
                httpretty.GET,
                utils.get_url(self.API_BASE, endpoint),
                body=content,
            )

        # register all the field endpoints
        _register(
            'field_titles/developments',
            fixture='development_fields_en.json',
        )
        _register(
            'field_order/developments',
            fixture='development_fields_order.json',
        )
        _register(
            'field_titles/development_groups',
            fixture='group_fields_en.json',
        )
        _register(
            'field_order/development_groups',
            fixture='group_fields_order.json',
        )
        _register(
            'field_titles/development_phases',
            fixture='phase_fields_en.json',
        )
        _register(
            'field_order/development_phases',
            fixture='phase_fields_order.json',
        )

        # register the development endpoints
        _register(
            'developments',
            fixture='integration/development_list_26-1.json',
        )
