# -*- coding: utf-8 -*-
"""Test the result classes."""

# local imports
from mls.apiclient import api, results
from mls.apiclient.tests import base


class ResultTestCase(base.BaseTestCase):
    """Test result class."""

    def setUp(self):
        self.api = api.API(self.BASE_URL)

    def _callFUT(self, api, data, settings=None):
        return results.Result(api, data, settings=settings)

    def test_wrong_data(self):
        """Validate the ValueError if data is not a dictionary."""
        self.assertRaises(ValueError, self._callFUT, self.api, None)
        self.assertRaises(ValueError, self._callFUT, self.api, 1)
        self.assertRaises(ValueError, self._callFUT, self.api, 1.1)
        self.assertRaises(ValueError, self._callFUT, self.api, True)
        self.assertRaises(ValueError, self._callFUT, self.api, 'Foo')
        self.assertRaises(ValueError, self._callFUT, self.api, u'Foo')

    def test_correct_data(self):
        """Validate the correct initialization with a dictionary."""
        data = {
            'response': {
                'foo': 'bar',
            },
        }
        foo = self._callFUT(self.api, data)
        self.assertIsInstance(foo, results.Result)
        self.assertEqual(data.get('response'), foo._data)

    def test_attributes(self):
        """Validate the content of the data dictionary."""
        data = {
            'response': {
                'foo': 'bar',
            },
        }
        foo = self._callFUT(self.api, data)
        self.assertEqual(foo.foo, 'bar')

    def test_missing_attributes(self):
        """Validate that an error is raised when an attribute is missing."""
        data = {
            'response': {
                'foo': 'bar',
            },
        }
        foo = self._callFUT(self.api, data)
        self.assertRaises(AttributeError, getattr, foo, 'bar')

    def test_get_attributes(self):
        """Validate the output of the get_attributes method."""
        data = {
            'response': {
                'foo': 'bar',
                'baz': 'barbar',
            },
        }
        foo = self._callFUT(self.api, data)
        result = foo.get_attributes()
        self.assertIn('foo', result)
        self.assertIn('baz', result)
        self.assertEqual(len(result), 2)

    def test_get_id(self):
        """Validate the output of the get_id method."""
        foo = self._callFUT(self.api, {})
        self.assertIsNone(foo.get_id())

        data = {
            'id': 'my_id',
        }
        foo = self._callFUT(self.api, data)
        self.assertEqual(foo.get_id(), 'my_id')

    def test_get_url(self):
        """Validate the output of the get_url method."""
        foo = self._callFUT(self.api, {})
        self.assertIsNone(foo.get_url())

        data = {
            'url': 'http://example.com',
        }
        foo = self._callFUT(self.api, data)
        self.assertEqual(foo.get_url(), 'http://example.com')

    def test_settings(self):
        """Validate the settings."""
        foo = self._callFUT(self.api, {}, settings=None)
        self.assertEqual(foo._settings, {})

        foo = self._callFUT(self.api, {}, settings={'foo': 'bar'})
        self.assertEqual(foo._settings, {'foo': 'bar'})

        self.assertRaises(ValueError, self._callFUT, self.api, {}, settings=1)
        self.assertRaises(ValueError, self._callFUT, self.api, {}, settings=1.1)
        self.assertRaises(ValueError, self._callFUT, self.api, {}, settings=True)
        self.assertRaises(ValueError, self._callFUT, self.api, {}, settings='Foo')
        self.assertRaises(ValueError, self._callFUT, self.api, {}, settings=u'Foo')


class AgencyTestCase(base.BaseTestCase):
    """Test 'Agency' result class."""

    def setUp(self):
        self.api = api.API(self.BASE_URL)

    def _callFUT(self, api, data, settings=None):
        return results.Agency(api, data, settings=settings)

    def test_listings(self):
        """Validate the listing search for agencies."""
        agency = self._callFUT(self.api, {})
        self.assertRaises(NotImplementedError, agency.listings)

    def test_developments(self):
        """Validate the development search for agencies."""
        agency = self._callFUT(self.api, {})
        self.assertRaises(NotImplementedError, agency.developments)


class AgentTestCase(base.BaseTestCase):
    """Test 'Agent' result class."""

    def setUp(self):
        self.api = api.API(self.BASE_URL)

    def _callFUT(self, api, data, settings=None):
        return results.Agent(api, data, settings=settings)

    def test_listings(self):
        """Validate the listing search for agents."""
        agent = self._callFUT(self.api, {})
        self.assertRaises(NotImplementedError, agent.listings)


class DevelopmentTestCase(base.BaseTestCase):
    """Test 'Development' result class."""

    def setUp(self):
        self.api = api.API(self.BASE_URL)

    def _callFUT(self, api, data, settings=None):
        return results.Development(api, data, settings=settings)

    def test_listings(self):
        """Validate the listing search for developments."""
        development = self._callFUT(self.api, {})
        self.assertRaises(NotImplementedError, development.listings)

    def test_pictures(self):
        """Validate the pictures for developments."""
        development = self._callFUT(self.api, {})
        self.assertRaises(NotImplementedError, development.pictures)

    def test_property_groups(self):
        """Validate the property group search for developments."""
        development = self._callFUT(self.api, {})
        self.assertRaises(NotImplementedError, development.groups)

    def test_development_phases(self):
        """Validate the development phase search for developments."""
        development = self._callFUT(self.api, {})
        self.assertRaises(NotImplementedError, development.phases)


class DevelopmentPhaseTestCase(base.BaseTestCase):
    """Test 'Development Phase' result class."""

    def setUp(self):
        self.api = api.API(self.BASE_URL)

    def _callFUT(self, api, data, settings=None):
        return results.DevelopmentPhase(api, data, settings=settings)

    def test_listings(self):
        """Validate the listing search for development phases."""
        phase = self._callFUT(self.api, {})
        self.assertRaises(NotImplementedError, phase.listings)


class ListingTestCase(base.BaseTestCase):
    """Test 'Listing' result class."""

    def setUp(self):
        self.api = api.API(self.BASE_URL)

    def _callFUT(self, api, data, settings=None):
        return results.Listing(api, data, settings=settings)

    def test_pictures(self):
        """Validate the pictures for listings."""
        listing = self._callFUT(self.api, {})
        self.assertRaises(NotImplementedError, listing.pictures)


class PropertyGroupTestCase(base.BaseTestCase):
    """Test 'Property Group' result class."""

    def setUp(self):
        self.api = api.API(self.BASE_URL)

    def _callFUT(self, api, data, settings=None):
        return results.PropertyGroup(api, data, settings=settings)

    def test_listings(self):
        """Validate the listing search for property groups."""
        group = self._callFUT(self.api, {})
        self.assertRaises(NotImplementedError, group.listings)
