# -*- coding: utf-8 -*-

###############################################################################
#
# Copyright (c) 2011 Propertyshelf, Inc. and its Contributors.
# All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by the
# Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
###############################################################################
"""MLS API Client implementation.

mls.apiclient is a Python client for the RESTful API of the Propertyshelf MLS.
"""

from anyjson import deserialize
import urllib
import urllib2
from urlparse import urljoin

from mls.apiclient.exceptions import ObjectNotFound, ImproperlyConfigured, MLSError

API_URL = 'api'


class ResourceBase(object):
    """Base resource class."""

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

    def get(self, listing_id, lang=None):
        """Returns one object of this Resource.

        You have to give one keyword argument to find the object.
        """
        kwargs = {}
#         if not len(kwargs) == 1:
#             raise MLSError('You have to give exactly one argument.')
#         if 'limit' in kwargs:
#             raise MLSError('There is no sense in using limit with get.')
#         if 'offset' in kwargs:
#             raise MLSError('There is no sense in using offset with get.')
        kwargs['search'] = 'listing/%s' % listing_id
        if lang is not None:
            kwargs['lang'] = lang
        result = self._query(kwargs, batching=False)
        if result is None:
            raise ObjectNotFound('Listing not found.')
        return result

    def search(self, kwargs):
        """Returns a list of objects.

        You can search for objects by giving one or more keyword arguments.
        Use limit and offset to limit the results.
        """
        if len(kwargs) == 0:
            raise MLSError('You have to give at least one search argument.')
        kwargs['search'] = 'search'
        results, batching = self._query(kwargs)
        return results, batching

    def _query(self, kwargs, batching=True):
        """Generates the URL and sends the HTTP request to the MLS."""
        url = self._url
        search = kwargs.pop('search', '')
        if search:
            url = urljoin(url + '/', search)
        kwargs['apikey'] = self._api_key
        kwargs['format'] = self._format
        encoded_args = urllib.urlencode(kwargs)
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


class AuctionListingsResource(ResourceBase):
    """Auction Listings Resource."""
    path = 'auction'


class ImagesResource(ResourceBase):
    """Images Resource."""
    path = 'images'


class AgencyResource(ResourceBase):
    """Agency Resource."""
    path = 'agencies'
