# -*- coding: utf-8 -*-
"""Several test utils."""

# python imports
import os


def get_url(base_url, endpoint):
    """Return URL for endpoint."""
    return '/'.join([
        base_url,
        endpoint,
    ])


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


def wrap_content(content, status_code=200, headers={}):
    """Wrap content into JSON structure.

    Wrap string JSON content in the appropriate response format with the
    given status code and return the JSON response as a string.
    """
    return u'{{"status": {0}, "headers": {1}, "response": {2}}}'.format(
        status_code,
        headers,
        content,
    )


def setup_fixtures():
    """Register fixtures for the MLS API."""
    from mls.apiclient import testing

    # Register field_titles endpoints
    testing._register(
        'field_titles/development_phases',
        params=testing.BASE_PARAMS,
        fixture='field_titles-development_phases.json',
    )
    testing._register(
        'field_titles/developments',
        params=testing.BASE_PARAMS,
        fixture='field_titles-developments.json',
    )
    testing._register(
        'field_titles/property_groups',
        params=testing.BASE_PARAMS,
        fixture='field_titles-property_groups.json',
    )

    # Register field_order endpoints
    testing._register(
        'field_order/development_phases',
        params=testing.BASE_PARAMS,
        fixture='field_order-development_phases.json',
    )
    testing._register(
        'field_order/developments',
        params=testing.BASE_PARAMS,
        fixture='field_order-developments.json',
    )
    testing._register(
        'field_order/property_groups',
        params=testing.BASE_PARAMS,
        fixture='field_order-property_groups.json',
    )


def setup_listing_api_fixtures():
    """Register fixtures for the MLS Listing API."""
    from mls.apiclient import testing

    # Register categories endpoints
    testing._register_api_listings(
        'categories/geographic_types',
        params=dict(
            {
                'format': 'json',
            },
            **testing.BASE_PARAMS),
        fixture='listings-categories-geographic_types.json',
    )
    testing._register_api_listings(
        'categories/listing_types',
        params=dict(
            {
                'format': 'json',
            },
            **testing.BASE_PARAMS),
        fixture='listings-categories-listing_types.json',
    )
    testing._register_api_listings(
        'categories/location_county',
        params=dict(
            {
                'format': 'json',
            },
            **testing.BASE_PARAMS),
        fixture='listings-categories-location_county.json',
    )
    testing._register_api_listings(
        'categories/location_district',
        params=dict(
            {
                'format': 'json',
            },
            **testing.BASE_PARAMS),
        fixture='listings-categories-location_district.json',
    )
    testing._register_api_listings(
        'categories/location_state',
        params=dict(
            {
                'format': 'json',
            },
            **testing.BASE_PARAMS),
        fixture='listings-categories-location_state.json',
    )
    testing._register_api_listings(
        'categories/location_types',
        params=dict(
            {
                'format': 'json',
            },
            **testing.BASE_PARAMS),
        fixture='listings-categories-location_types.json',
    )
    testing._register_api_listings(
        'categories/object_types',
        params=dict(
            {
                'format': 'json',
            },
            **testing.BASE_PARAMS),
        fixture='listings-categories-object_types.json',
    )
    testing._register_api_listings(
        'categories/ownership_types',
        params=dict(
            {
                'format': 'json',
            },
            **testing.BASE_PARAMS),
        fixture='listings-categories-ownership_types.json',
    )
    testing._register_api_listings(
        'categories/view_types',
        params=dict(
            {
                'format': 'json',
            },
            **testing.BASE_PARAMS),
        fixture='listings-categories-view_types.json',
    )

    # Register listing search endpoints
    testing._register_api_listings(
        'search',
        params=dict(
            {
                'reverse': 1,
                'sort_on': 'last_activated_date',
                'format': 'json',
                'limit': 25,
                'offset': 0,
            },
            **testing.BASE_PARAMS),
        fixture='listings-search-sort_on__last_activated-reverse.json',
    )
