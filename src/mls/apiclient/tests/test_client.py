# -*- coding: utf-8 -*-
"""Test the response handling of the Propertyshelf MLS client."""

from mls.apiclient.client import ListingResource
from mls.apiclient.tests import base
from mls.apiclient.tests import utils

import json
import responses


class TestEnvelopeExtras(base.BaseTestCase):
    """Test that response envelope extras end up in the result data.

    The MLS returns some values next to 'result' instead of inside of it.
    They describe the requested item, so the client merges them into the
    result data.
    """

    PATH = '/api/listings'
    LISTING_ID = 'agency-id-1'
    NOTICE = (
        u'Listing provided by Test Agency in cooperation with MLS-Ecuador. '
        u'\xa9 2026 Propertyshelf Inc. All rights reserved.'
    )

    def setUp(self):
        responses.start()

    def tearDown(self):
        responses.stop()
        responses.reset()

    def _add_response(self, body):
        responses.add(
            responses.GET,
            utils.get_url(self.URL, '/'.join(['listing', self.LISTING_ID])),
            body=json.dumps(body),
        )

    def test_listing_attribution_is_merged_into_result(self):
        self._add_response({
            'status': 'ok',
            'result': {'listing': {'id': self.LISTING_ID}},
            'listing_attribution': self.NOTICE,
        })
        client = ListingResource(self.BASE_URL)
        result = client.get(self.LISTING_ID)
        assert result.get('listing_attribution') == self.NOTICE
        # The listing data itself is left untouched.
        assert result.get('listing') == {'id': self.LISTING_ID}

    def test_missing_listing_attribution_is_not_added(self):
        self._add_response({
            'status': 'ok',
            'result': {'listing': {'id': self.LISTING_ID}},
        })
        client = ListingResource(self.BASE_URL)
        result = client.get(self.LISTING_ID)
        assert 'listing_attribution' not in result

    def test_non_dict_result_is_returned_unchanged(self):
        self._add_response({
            'status': 'ok',
            'result': ['a', 'b'],
            'listing_attribution': self.NOTICE,
        })
        client = ListingResource(self.BASE_URL)
        assert client.get(self.LISTING_ID) == ['a', 'b']
