# -*- coding: utf-8 -*-
"""Test API class."""

# python imports
import httpretty
import requests

# local imports
from mls.apiclient import api, exceptions
from mls.apiclient.tests import base, utils


class TestAPI(base.BaseTestCase):
    """API test case."""
    PATH = '/api/rest/v1/developments'

    def setUp(self):
        self.api = self._callFUT(self.BASE_URL)

    def _callFUT(self, base_url, api_key=None, lang=None, debug=False):
        return api.API(base_url, api_key=api_key, lang=lang, debug=debug)

    def test_class(self):
        """Validate the class initialization and attributes."""
        api = self._callFUT(
            self.BASE_URL,
            api_key='1234567890abcdef',
            lang='de',
            debug=True,
        )
        self.assertEqual(api.base_url, self.BASE_URL)
        self.assertEqual(api.api_key, '1234567890abcdef')
        self.assertEqual(api.lang, 'de')
        self.assertTrue(api.debug)

    def test_headers(self):
        """Validate the ``headers`` method."""
        headers = self.api.headers()
        self.assertEqual(len(headers.keys()), 2)
        self.assertEqual(headers['Content-Type'], 'application/json')
        self.assertEqual(headers['Accept'], 'application/json')

    @httpretty.httprettified
    def test_handle_http_response_200(self):
        """Validate a HTTP 200 code."""
        content = u'{"some": "content"}'
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            status=200,
        )
        response = requests.get(self.URL)
        result = self.api.handle_response(response, content)
        self.assertEqual(result, {'some': 'content'})

        result = self.api.handle_response(response, None)
        self.assertEqual(result, {})

        self.assertRaises(
            ValueError,
            self.api.handle_response, response, u'No JSON',
        )

    @httpretty.httprettified
    def test_handle_api_response_200(self):
        """Validate a API 200 code."""
        content = utils.wrap_content(u'{"some": "content"}', status_code=200)
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            body=content,
            status=200,
        )
        response = requests.get(self.URL)
        result = self.api.handle_response(response, content)
        response_body = result.get('response')
        self.assertEqual(response_body, {'some': 'content'})

    @httpretty.httprettified
    def test_handle_http_response_30x(self):
        """Validate a HTTP 30x code."""
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            status=301,
        )
        response = requests.get(self.URL)
        self.assertRaises(
            exceptions.Redirection,
            self.api.handle_response, response, None,
        )

    @httpretty.httprettified
    def test_handle_api_response_30x(self):
        """Validate a API 30x code."""
        content = utils.wrap_content(u'"Redirect"', status_code=301)
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            body=content,
            status=200,
        )
        response = requests.get(self.URL)
        self.assertRaises(
            exceptions.Redirection,
            self.api.handle_response, response, content,
        )

    @httpretty.httprettified
    def test_handle_http_response_400(self):
        """Validate a HTTP 400 code."""
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            status=400,
        )
        response = requests.get(self.URL)
        self.assertRaises(
            exceptions.BadRequest,
            self.api.handle_response, response, None,
        )

    @httpretty.httprettified
    def test_handle_api_response_400(self):
        """Validate a API 400 code."""
        content = utils.wrap_content(u'"Bad request"', status_code=400)
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            body=content,
            status=200,
        )
        response = requests.get(self.URL)
        self.assertRaises(
            exceptions.BadRequest,
            self.api.handle_response, response, content,
        )

    @httpretty.httprettified
    def test_handle_http_response_401(self):
        """Validate a HTTP 401 code."""
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            status=401,
        )
        response = requests.get(self.URL)
        self.assertRaises(
            exceptions.UnauthorizedAccess,
            self.api.handle_response, response, None,
        )

    @httpretty.httprettified
    def test_handle_api_response_401(self):
        """Validate a API 401 code."""
        content = utils.wrap_content(u'"Unauthorized access"', status_code=401)
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            body=content,
            status=200,
        )
        response = requests.get(self.URL)
        self.assertRaises(
            exceptions.UnauthorizedAccess,
            self.api.handle_response, response, content,
        )

    @httpretty.httprettified
    def test_handle_http_response_500(self):
        """Validate a HTTP 500 code."""
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            status=500,
        )
        response = requests.get(self.URL)
        self.assertRaises(
            exceptions.ServerError,
            self.api.handle_response, response, None,
        )

    @httpretty.httprettified
    def test_handle_api_response_500(self):
        """Validate a API 500 code."""
        content = utils.wrap_content(u'"Server Error"', status_code=500)
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            body=content,
            status=200,
        )
        response = requests.get(self.URL)
        self.assertRaises(
            exceptions.ServerError,
            self.api.handle_response, response, content,
        )

    @httpretty.httprettified
    def test_get(self):
        """Validate the ``get`` method."""
        content = u'{"some": "content"}'
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            body=content,
            status=200,
        )
        result = self.api.get(self.PATH)
        self.assertEqual(result, {'some': 'content'})

    @httpretty.httprettified
    def test_http_call(self):
        """Validate the ``http_call`` method."""
        content = u'{"some": "content"}'
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            body=content,
            status=200,
        )
        result = self.api.http_call(self.URL, 'GET')
        self.assertEqual(result, {'some': 'content'})

    @httpretty.httprettified
    def test_request(self):
        """Validate the ``request`` method."""
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            body='{}',
            status=200,
        )
        result = self.api.request(self.URL, 'GET')
        self.assertEqual(result, {})

        content = u'{"some": "content"}'
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            body=content,
            status=200,
        )
        result = self.api.request(self.URL, 'GET')
        self.assertEqual(result, {'some': 'content'})

    @httpretty.httprettified
    def test_api_debug(self):
        content = u'{"debug": true}'
        api_debug = self._callFUT(self.BASE_URL, debug=True)
        httpretty.register_uri(
            httpretty.GET,
            self.URL,
            body=content,
            status=200,
        )
        result = api_debug.request(self.URL, 'GET')
        self.assertEqual(result, {'debug': True})
