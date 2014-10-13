# -*- coding: utf-8 -*-
"""Client for the restful MLS API."""


REST_API_URL = 'api/rest'
REST_API_VERSION = 'v1'


class Resource(object):
    """Base resource for the restful MLS API."""

    endpoint = None

    def __init__(self, api, path=None, debug=False):
        self.api = api
        self.path = path
        self.debug = debug

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

    def fields(self, lang=None):
        """Returns a list of available fields for this resource."""
        raise NotImplementedError

    def _return_value(self, fields, data):
        return dict([(
            f, {'label': fields.get(f, f), 'value': data.get(f, None)}
        ) for f in data.keys()])


class Developments(Resource):
    """'Development Project' resource."""

    endpoint = 'developments'
