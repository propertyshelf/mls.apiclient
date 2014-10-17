# -*- coding: utf-8 -*-
"""MLS rest client entity resource classes."""

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
        self._data = data.get('response', {})
        self._id = data.get('id', None)
        self._url = data.get('url', None)
        self._debug = debug
        self._endpoint_url = '{0}/{1}/{2}'.format(
            REST_API_URL,
            REST_API_VERSION,
            self.endpoint,
        )

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

    def get(self, key, lang=None):
        """Returns one object of this Resource.

        You have to give one keyword argument to find the object.
        """
        raise NotImplementedError

    def search(self, params):
        """Returns a list of objects.

        You can search for objects by giving one or more keyword arguments.
        Use limit and offset to limit the results.
        """
        raise NotImplementedError

    def get_attributes(self):
        """Returns a list of all attributes of a Resource object."""
        return self._data.keys()

    def get_id(self):
        """Returns the id of the resource object."""
        return self._id

    def get_url(self):
        """Returns the URL to the resource object."""
        return self._url

    def get_field_titles(self, lang=None):
        """Return the translated titles of the fields."""
        url = '{0}/{1}'.format(self._endpoint_url, 'fields')
        return self._api.get(url)

    def get_fieldnames_in_order(self):
        """Return the list of fieldnames in order as defined in the MLS."""
        raise NotImplementedError

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

    def listings(self):
        """Search for listings assigned to that property group."""
        raise NotImplementedError
