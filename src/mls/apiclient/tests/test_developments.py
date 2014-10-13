# -*- coding: utf-8 -*-
"""Test development project resources."""

# python imports
import httpretty

# local imports
from mls.apiclient import api
from mls.apiclient.resources import Developments
from mls.apiclient.tests import base, utils


class TestDevelopments(base.BaseTestCase):
    """Development project test case."""
    PATH = '/api/rest/v1/developments'

    def setUp(self):
        self.api = api.API(self.BASE_URL)

    @httpretty.httprettified
    def test_list(self):
        """Validate the 'list developments' endpoint."""
        resource = ''
        httpretty.register_uri(
            httpretty.GET,
            utils.get_url(self.URL, resource),
            body=utils.load_fixture('development_list_en.json')
        )
        client = Developments(api=self.api)
        params = {}
        self.assertRaises(NotImplementedError, client.search, params)

    @httpretty.httprettified
    def test_fields(self):
        """Validate the 'fields' endpoint."""
        resource = 'fields'
        httpretty.register_uri(
            httpretty.GET,
            utils.get_url(self.URL, resource),
            body=utils.load_fixture('development_fields_en.json')
        )
        client = Developments(api=self.api)
        self.assertRaises(NotImplementedError, client.fields)
