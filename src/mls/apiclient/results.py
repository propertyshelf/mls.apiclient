# -*- coding: utf-8 -*-
"""MLS rest client entity result classes."""


class Result(object):
    """Base class for results."""

    def __init__(self, data, settings=None):
        if not isinstance(data, dict):
            raise ValueError(
                'Data must be dictionary with content of the result.'
            )

        self._data = data.get('response', {})
        self._id = data.get('id', None)
        self._url = data.get('url', None)

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

    def get_attributes(self):
        """Returns a list of all attributes of a Result object."""
        return self._data.keys()

    def get_id(self):
        """Returns the id of the result object."""
        return self._id

    def get_url(self):
        """Returns the URL to the result object."""
        return self._url


class Agency(Result):
    """'Agency' entity result class."""


class Agent(Result):
    """'Agent' entity result class."""


class Development(Result):
    """'Development Project' entity result class."""


class DevelopmentPhase(Result):
    """'Development Phase' entity result class."""


class Listing(Result):
    """'Listing' entity result class."""


class PropertyGroup(Result):
    """'Property Group' entity result class."""
