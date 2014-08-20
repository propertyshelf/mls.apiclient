# -*- coding: utf-8 -*-
"""Test the result classes."""

# python imports
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# local imports
from mls.apiclient import results


class ResultTestCase(unittest.TestCase):
    """Test result class."""

    def _callFUT(self, data):
        return results.Result(data)

    def test_wrong_data(self):
        """Validate the ValueError if data is not a dictionary."""
        self.assertRaises(ValueError, self._callFUT, None)
        self.assertRaises(ValueError, self._callFUT, 1)
        self.assertRaises(ValueError, self._callFUT, 1.1)
        self.assertRaises(ValueError, self._callFUT, True)
        self.assertRaises(ValueError, self._callFUT, 'Foo')
        self.assertRaises(ValueError, self._callFUT, u'Foo')

    def test_correct_data(self):
        """Validate the correct initialization with a dictionary."""
        data = {
            'response': {
                'foo': 'bar',
            },
        }
        foo = self._callFUT(data)
        self.assertIsInstance(foo, results.Result)
        self.assertEqual(data.get('response'), foo._data)

    def test_attributes(self):
        data = {
            'response': {
                'foo': 'bar',
            },
        }
        foo = self._callFUT(data)
        self.assertEqual(foo.foo, 'bar')

    def test_missing_attributes(self):
        data = {
            'response': {
                'foo': 'bar',
            },
        }
        foo = self._callFUT(data)
        self.assertRaises(AttributeError, getattr, foo, 'bar')

    def test_get_attributes(self):
        """Validate the output of the get_attributes method."""
        data = {
            'response': {
                'foo': 'bar',
                'baz': 'barbar',
            },
        }
        foo = self._callFUT(data)
        result = foo.get_attributes()
        self.assertIn('foo', result)
        self.assertIn('baz', result)
        self.assertEqual(len(result), 2)

    def test_get_id(self):
        """Validate the output of the get_id method."""
        foo = self._callFUT({})
        self.assertIsNone(foo.get_id())

        data = {
            'id': 'my_id',
        }
        foo = self._callFUT(data)
        self.assertEqual(foo.get_id(), 'my_id')

    def test_get_url(self):
        """Validate the output of the get_url method."""
        foo = self._callFUT({})
        self.assertIsNone(foo.get_url())

        data = {
            'url': 'http://example.com',
        }
        foo = self._callFUT(data)
        self.assertEqual(foo.get_url(), 'http://example.com')
