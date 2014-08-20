# -*- coding: utf-8 -*-
"""MLS rest client entity result classes."""


class Result(object):
    """Base class for results."""

    def __init__(self, data):
        if not isinstance(data, dict):
            raise ValueError(
                'Data must be dictionary with content of the result'
            )

        self._data = data.get('response', {})
    def __getattr__(self, name):
        """Returns an data attribute or raises AttributeError."""
        try:
            return self._data[name]
        except KeyError:
            return object.__getattribute__(self, name)

    def get_attributes(self):
        """Returns a list of all attributes of a Result object."""
        return self._data.keys()


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
