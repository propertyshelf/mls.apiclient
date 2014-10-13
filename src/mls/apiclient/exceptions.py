# -*- coding: utf-8 -*-
"""mls.apiclient exception classes."""


class MLSError(Exception):
    """Main exception class."""
    pass


class ImproperlyConfigured(MLSError):
    """This exception is raised on configuration errors."""
    pass


class ObjectNotFound(MLSError):
    """This exception is raised if an object can not be found."""
    pass


class MultipleResults(MLSError):
    """This exception is raised on multiple results.

    That is, if a get request returns more than one result.
    """
    def __str__(self):
        return 'Your query had multiple results.'


class ConnectionError(Exception):
    """Base exception for any type of connection error with the requests."""

    def __init__(self, response, content=None, message=None):
        self.response = response
        self.content = content
        self.message = message

    def __str__(self):
        message = 'Failed.'
        if hasattr(self.response, 'status_code'):
            message += ' Response status: {0}.'.format(
                self.response.status_code
            )
        if hasattr(self.response, 'reason'):
            message += ' Response message: {0}.'.format(self.response.reason)
        if self.content is not None:
            message += ' Error message: ' + str(self.content)
        return message


class ClientError(ConnectionError):
    """4xx Client Error."""
    pass


class BadRequest(ClientError):
    """400 Bad Request."""
    pass


class UnauthorizedAccess(ClientError):
    """401 Unauthorized."""
    pass


class ServerError(ConnectionError):
    """5xx Server Error."""
    pass
