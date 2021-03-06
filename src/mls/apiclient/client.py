# -*- coding: utf-8 -*-
"""MLS API Client implementation.

mls.apiclient is a Python client for the RESTful API of the Propertyshelf MLS.
"""

from copy import deepcopy
from mls.apiclient.exceptions import ImproperlyConfigured
from mls.apiclient.exceptions import MLSError
from mls.apiclient.exceptions import ObjectNotFound
from urlparse import urljoin

import datetime
import logging
import requests


API_URL = 'api'

#: Disable noisy messages from requests module.
requests_log = logging.getLogger('requests')
requests_log.setLevel(logging.WARNING)

logger = logging.getLogger('mls.apiclient.client')


class ResourceBase(object):
    """Base resource class."""

    path = None
    path_search = 'search'
    path_detail = 'detail'
    path_categories = None

    def __init__(self, base_url, api_key='', path=None, debug=False):
        self._base_url = base_url
        self._api_key = api_key
        self._debug = debug
        if path:
            self.path = path
        self._url = '/'.join([self._base_url, API_URL, self.path])
        self._format = 'json'

    def all(self):
        """Returns all objects of this Resource."""
        return self._query()

    def get(self, key, lang=None, params=None):
        """Returns one object of this Resource.

        You have to give one keyword argument to find the object.
        """
        if not params or not isinstance(params, dict):
            params = {}
        params['search'] = '/'.join([self.path_detail, key])
        if lang is not None:
            params['lang'] = lang
        result = self._query(params, batching=False)
        if result is None:
            raise ObjectNotFound('Item not found.')
        return result

    def category(self, key, lang=None):
        """Return values for a categorie."""
        if self.path_categories is None:
            return
        params = {}
        params['search'] = '/'.join([self.path_categories, key])
        if lang is not None:
            params['lang'] = lang
        result = self._query(params, batching=False)
        if result is None:
            raise ObjectNotFound('Item not found.')
        return [tuple(item) for item in result]

    def search(self, params):
        """Returns a list of objects.

        You can search for objects by giving one or more keyword arguments.
        Use limit and offset to limit the results.
        """
        if len(params) == 0:
            raise MLSError('You have to give at least one search argument.')
        params['search'] = self.path_search
        results, batching = self._query(params)
        return results, batching

    def _get_response(self, url, params, timeout=2.5):
        """Get the response from the MLS.

        :param url: [required] Request URL.
        :type url: string
        :param params: [required] Request params.
        :type params: dict
        :param timeout: Request timeout.
        :type timeout: float
        :returns: response
        :rtype: requests.response object
        """
        if self._debug:
            start_time = datetime.datetime.now()

        verify_ssl = True
        while True:
            try:
                r = requests.get(url, params=params, timeout=timeout, verify=verify_ssl)
            except requests.exceptions.SSLError, e:
                verify_ssl = False
                continue
            except requests.exceptions.ConnectionError, e:
                if e.request:
                    raise MLSError(
                        'Connection to the MLS at {0} failed.'.format(
                            e.request.url,
                        )
                    )
                else:
                    raise MLSError(e)
            except requests.exceptions.MissingSchema:
                raise MLSError(
                    'No or wrong MLS URL provided.'
                )
            except requests.exceptions.Timeout, e:
                raise MLSError(
                    'Connection to the MLS at {0} timed out.'.format(e.request.url)
                )
            else:
                break

        if self._debug:
            logger.info('Request: {0}'.format(r.url))
            duration = datetime.datetime.now() - start_time
            logger.info('Response[{0}]: {1}, Duration: {2}.{3}s.'.format(
                r.status_code,
                r.reason,
                duration.seconds,
                duration.microseconds,
            ))
        return r

    def _query(self, _params, batching=True):
        """Generates the URL and sends the HTTP request to the MLS."""
        url = self._url
        params = deepcopy(_params)
        search = params.pop('search', '')
        if search:
            url = urljoin(url + '/', search)
        params['apikey'] = self._api_key
        params['format'] = self._format
        # encoded_args = urllib.urlencode(params)
        # url = url + '?' + encoded_args

        r = self._get_response(url, params)

        try:
            response = r.json()
        except ValueError:
            raise MLSError(
                'The data returned from the server could not be read.'
            )

        if response.get('status', None) != 'ok':
            raise ImproperlyConfigured('Wrong request ({0}).'.format(r.url))

        results = response.get('result', None)
        if not batching:
            return results

        batching = response.get('batching', None)
        batch = None
        if batching and batching.get('active', False):
            batch = {
                'results': batching.get('results_total', 0),
                'items': batching.get('results_page', 0),
                'next': batching.get('next', None),
                'prev': batching.get('prev', None)
            }
        return results, batch


class ListingResource(ResourceBase):
    """Listings Resource."""
    path = 'listings'
    path_search = 'search'
    path_detail = 'listing'
    path_categories = 'categories'
