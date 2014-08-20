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

    def _callFUT(self, data, settings=None):
        return results.Result(data, settings=settings)

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
        """Validate the content of the data dictionary."""
        data = {
            'response': {
                'foo': 'bar',
            },
        }
        foo = self._callFUT(data)
        self.assertEqual(foo.foo, 'bar')

    def test_missing_attributes(self):
        """Validate that an error is raised when an attribute is missing."""
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

    def test_settings(self):
        """Validate the settings."""
        foo = self._callFUT({}, settings=None)
        self.assertEqual(foo._settings, {})

        foo = self._callFUT({}, settings={'foo': 'bar'})
        self.assertEqual(foo._settings, {'foo': 'bar'})

        self.assertRaises(ValueError, self._callFUT, {}, settings=1)
        self.assertRaises(ValueError, self._callFUT, {}, settings=1.1)
        self.assertRaises(ValueError, self._callFUT, {}, settings=True)
        self.assertRaises(ValueError, self._callFUT, {}, settings='Foo')
        self.assertRaises(ValueError, self._callFUT, {}, settings=u'Foo')


class AgencyTestCase(unittest.TestCase):
    """Test 'Agency' result class."""

    def _callFUT(self, data, settings=None):
        return results.Agency(data, settings=settings)

    def test_listings(self):
        """Validate the listing search for agencies."""
        agency = self._callFUT({})
        self.assertRaises(NotImplementedError, agency.listings)

    def test_developments(self):
        """Validate the development search for agencies."""
        agency = self._callFUT({})
        self.assertRaises(NotImplementedError, agency.developments)


class AgentTestCase(unittest.TestCase):
    """Test 'Agent' result class."""

    def _callFUT(self, data, settings=None):
        return results.Agent(data, settings=settings)

    def test_listings(self):
        """Validate the listing search for agents."""
        agent = self._callFUT({})
        self.assertRaises(NotImplementedError, agent.listings)


class DevelopmentTestCase(unittest.TestCase):
    """Test 'Development' result class."""

    def _callFUT(self, data, settings=None):
        return results.Development(data, settings=settings)

    def test_listings(self):
        """Validate the listing search for developments."""
        development = self._callFUT({})
        self.assertRaises(NotImplementedError, development.listings)

    def test_pictures(self):
        """Validate the pictures for developments."""
        development = self._callFUT({})
        self.assertRaises(NotImplementedError, development.pictures)

    def test_property_groups(self):
        """Validate the property group search for developments."""
        development = self._callFUT({})
        self.assertRaises(NotImplementedError, development.groups)

    def test_development_phases(self):
        """Validate the development phase search for developments."""
        development = self._callFUT({})
        self.assertRaises(NotImplementedError, development.phases)


class DevelopmentPhaseTestCase(unittest.TestCase):
    """Test 'Development Phase' result class."""

    def _callFUT(self, data, settings=None):
        return results.DevelopmentPhase(data, settings=settings)

    def test_listings(self):
        """Validate the listing search for development phases."""
        phase = self._callFUT({})
        self.assertRaises(NotImplementedError, phase.listings)


class ListingTestCase(unittest.TestCase):
    """Test 'Listing' result class."""

    def _callFUT(self, data, settings=None):
        return results.Listing(data, settings=settings)

    def test_pictures(self):
        """Validate the pictures for listings."""
        listing = self._callFUT({})
        self.assertRaises(NotImplementedError, listing.pictures)


class PropertyGroupTestCase(unittest.TestCase):
    """Test 'Property Group' result class."""

    def _callFUT(self, data, settings=None):
        return results.PropertyGroup(data, settings=settings)

    def test_listings(self):
        """Validate the listing search for property groups."""
        group = self._callFUT({})
        self.assertRaises(NotImplementedError, group.listings)
