# -*- coding: utf-8 -*-
"""MLS rest client entity resource classes."""

# local imports
from mls.apiclient import utils

REST_API_URL = 'api/rest'
REST_API_VERSION = 'v1'


class Resource(object):
    """Base class for resources."""

    endpoint = None

    def __init__(self, api, data, settings=None, debug=False):
        if not isinstance(data, dict):
            raise ValueError(
                'Data must be dictionary with content of the resource.'
            )

        self._api = api
        self._status = data.get('status', None)
        self._headers = data.get('headers', {})
        self._data = data.get('response', {})
        self._links = self._data.get('links', {})
        self._debug = debug

        if settings is None:
            settings = {}

        if not isinstance(settings, dict):
            raise ValueError(
                'Settings must be dictionary.'
            )
        self._settings = settings

    def __getattr__(self, name):
        """Returns a data attribute or raises AttributeError."""
        try:
            return self._data[name]
        except KeyError:
            return object.__getattribute__(self, name)

    @classmethod
    def get(cls, api, resource_id):
        """Returns one object of this Resource.

        You have to give one keyword argument to find the object.
        """
        url = '{0}/{1}'.format(cls.get_endpoint_url(), resource_id)
        return api.get(url)

    @classmethod
    def search(cls, api, params=None):
        """Returns a list of objects with optional search parameters.

        You can search for objects by giving one or more keyword arguments.
        Use limit and offset to limit the results.
        """
        url = cls.get_endpoint_url()
        return api.get(url, params)

    @classmethod
    def get_field_titles(cls, api):
        """Return the translated titles of the fields."""
        url = '{0}/{1}'.format(cls.get_endpoint_url(), 'fields')
        return api.get(url)

    @classmethod
    def get_fieldnames_in_order(cls, api):
        """Return the list of fieldnames in order as defined in the MLS."""
        raise NotImplementedError

    @classmethod
    def get_endpoint_url(cls):
        """Returns the URL to the resource object."""
        return '{0}/{1}/{2}'.format(
            REST_API_URL,
            REST_API_VERSION,
            cls.endpoint,
        )

    def get_attributes(self):
        """Returns a list of all attributes of a Resource object."""
        return self._data.keys()

    def get_id(self):
        """Returns the id of the resource object."""
        return self._data.get('id', None)

    def get_url(self):
        """Returns the URL to the resource object."""
        return utils.get_link(self._links, 'self')

    def get_status(self):
        """Returns the status of the response for this resource object."""
        return self._status

    def get_headers(self):
        return self._headers

    def _return_value(self, fields, data):
        return dict([(
            f, {'label': fields.get(f, f), 'value': data.get(f, None)}
        ) for f in data.keys()])


class Agency(Resource):
    """'Agency' entity resource class."""

    def listings(self):
        """Search for listings within that agency."""
        raise NotImplementedError

    def developments(self):
        """Search for developments within that agency."""
        raise NotImplementedError


class Agent(Resource):
    """'Agent' entity resource class."""

    def listings(self):
        """Search for listings for that agent."""
        raise NotImplementedError


class Development(Resource):
    """'Development Project' entity resource class."""

    endpoint = 'developments'

    def listings(self):
        """Search for listings assigned to that development project."""
        raise NotImplementedError

    def pictures(self):
        """Get the pictures for that development."""
        raise NotImplementedError

    def groups(self):
        """Search for property groups within that development."""
        raise NotImplementedError

    def phases(self):
        """Search for development phases within that development."""
        raise NotImplementedError


class DevelopmentPhase(Resource):
    """'Development Phase' entity resource class."""

    endpoint = 'phases'

    def listings(self):
        """Search for listings assigned to that development phase."""
        raise NotImplementedError


class Listing(Resource):
    """'Listing' entity resource class."""

    def pictures(self):
        """Get the pictures for that listing."""
        raise NotImplementedError


class PropertyGroup(Resource):
    """'Property Group' entity resource class."""

    endpoint = 'groups'

    def listings(self):
        """Search for listings assigned to that property group."""
        raise NotImplementedError
