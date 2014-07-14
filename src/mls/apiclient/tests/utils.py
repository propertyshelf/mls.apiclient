# -*- coding: utf-8 -*-
"""Several test utils."""

# python imports
import os


def get_url(base_url, endpoint):
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
