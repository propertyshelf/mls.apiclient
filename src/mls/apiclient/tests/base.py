# -*- coding: utf-8 -*-

# python imports
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class BaseTestCase(unittest.TestCase):
    HOST = 'demomls.com'
    PATH = '/api'

    @property
    def BASE_URL(self):
        return 'http://%s' % self.HOST

    @property
    def URL(self):
        return self.BASE_URL + self.PATH
