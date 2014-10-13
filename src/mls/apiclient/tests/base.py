# -*- coding: utf-8 -*-
"""Test case base class."""

# python imports
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class BaseTestCase(unittest.TestCase):
    """Test case base class."""
    HOST = 'demomls.com'
    PATH = '/api'

    @property
    def BASE_URL(self):
        return 'http://{0}'.format(self.HOST)

    @property
    def URL(self):
        return self.BASE_URL + self.PATH
