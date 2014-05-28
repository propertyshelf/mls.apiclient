# -*- coding: utf-8 -*-
"""Test Propertyshelf MLS listings API."""

# python imports
import httpretty
import os
import pytest

# local imports
from mls.apiclient.client import ListingResource

TEST_URL = 'http://demomls.com'


def load_fixture(name):
    """Return a file-like fixture, just like urlopen would."""
    fixture = open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'fixtures',
            name,
        ), 'r'
    )
    return fixture.read()


def get_url(endpoint):
    return '/'.join([
        TEST_URL,
        endpoint,
    ])


@pytest.mark.httpretty
def test_listing_types():
    httpretty.register_uri(
        httpretty.GET,
        get_url('api/listings/categories/listing_types'),
        body=load_fixture('category_listing_types_en.json')
    )
    res = ListingResource(TEST_URL)
    category = res.category('listing_types')
    assert httpretty.last_request().querystring == {
        'format': ['json'],
    }
    expected = [
        ('ll', 'Land Listing'),
        ('rl', 'Residential Lease'),
        ('rs', 'Residential Sale'),
    ]
    assert category == expected


@pytest.mark.httpretty
def test_view_types():
    httpretty.register_uri(
        httpretty.GET,
        get_url('api/listings/categories/view_types'),
        body=load_fixture('category_view_types_en.json')
    )
    res = ListingResource(TEST_URL)
    category = res.category('view_types')
    assert httpretty.last_request().querystring == {
        'format': ['json'],
    }
    expected = [
        ('beach_view', 'Beach View'),
    ]
    assert category == expected
