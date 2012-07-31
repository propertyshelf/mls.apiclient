# -*- coding: utf-8 -*-

###############################################################################
#
# Copyright (c) 2012 Propertyshelf, Inc. and its Contributors.
# All Rights Reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AS IS AND ANY EXPRESSED OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
###############################################################################
"""MLS API Client implementation.

mls.apiclient is a Python client for the RESTful API of the Propertyshelf MLS.
"""

from anyjson import deserialize
from copy import deepcopy
import urllib
import urllib2
from urlparse import urljoin

from mls.apiclient.exceptions import (ImproperlyConfigured, MLSError,
    ObjectNotFound)

API_URL = 'api'


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

    def get(self, key, lang=None):
        """Returns one object of this Resource.

        You have to give one keyword argument to find the object.
        """
        params = {}
        params['search'] = '%s/%s' % (self.path_detail, key)
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
        params['search'] = '%s/%s' % (self.path_categories, key)
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

    def _query(self, _params, batching=True):
        """Generates the URL and sends the HTTP request to the MLS."""
        url = self._url
        params = deepcopy(_params)
        search = params.pop('search', '')
        if search:
            url = urljoin(url + '/', search)
        params['apikey'] = self._api_key
        params['format'] = self._format
        encoded_args = urllib.urlencode(params)
        url = url + '?' + encoded_args
        if self._debug:
            import sys
            sys.stdout.write(url + '\n')
        try:
            response = urllib2.urlopen(url).read()
        except urllib2.URLError:
            raise MLSError("Connection to the MLS at '%s' failed." % self._url)

        try:
            response = deserialize(response)
        except ValueError:
            raise MLSError("Connection to the MLS at '%s' failed." % self._url)

        if response.get('status', None) != 'ok':
            raise ImproperlyConfigured('Wrong request.')

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
