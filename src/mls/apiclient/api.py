# -*- coding: utf-8 -*-

# python imports
import datetime
import json
import logging
import requests

# local imports
from mls.apiclient import PRODUCT_NAME
from mls.apiclient import exceptions, utils

logger = logging.getLogger(PRODUCT_NAME)


class Api(object):
    """API class for the MLS.

    "The class contains all the base methods for establishing and
    authenticating the connections and requests to the MLS database.
    """

    def __init__(self, base_url, api_key=None):
        """Create API object.

        Usage::

            >>> import from mls.apiclient import api
            >>> mls = api.Api('http://demomls.com')
        """
        self.base_url = base_url
        self.api_key = api_key

    def request(self, url, method, body=None, params=None):
        """Make HTTP call, formats response and does error handling.
        Uses http_call method in API class.
        """

        params = utils.merge_dict(
            params or {},
            {'apikey': self.api_key},
        )
        url = utils.join_url_params(url, params)

        try:
            return self.http_call(
                url,
                method,
                data=json.dumps(body),
                headers=self.headers(),
            )
        except exceptions.BadRequest as error:
            # Format Error message for bad request
            return {'error': json.loads(error.content)}

    def http_call(self, url, method, **kwargs):
        """Makes a http call. Logs response information."""

        logger.info('Request[{0}]: {1}'.format(method, url))
        start_time = datetime.datetime.now()

        response = requests.request(
            method,
            url,
            **kwargs
        )

        duration = datetime.datetime.now() - start_time
        logger.info('Response[{0}]: {1}, Duration: {2}.{3}s.'.format(
            response.status_code,
            response.reason,
            duration.seconds,
            duration.microseconds,
        ))

        return self.handle_response(response, response.content.decode('utf-8'))

    def handle_response(self, response, content):
        """Validate HTTP response."""

        status = response.status_code
        if 200 <= status <= 299:
            return json.loads(content) if content else {}
        elif status in (301, 302, 303, 307):
            raise exceptions.Redirection(response, content)
        elif status == 400:
            raise exceptions.BadRequest(response, content)
        elif status == 401:
            raise exceptions.UnauthorizedAccess(response, content)
        elif 500 <= status <= 599:
            raise exceptions.ServerError(response, content)
        else:
            raise exceptions.ConnectionError(
                response,
                content,
                'Unknown response code: #{response.code}',
            )

    def headers(self):
        """Default HTTP headers."""

        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def get(self, action, params=None):
        """Make GET request."""

        return self.request(
            utils.join_url(self.base_url, action),
            'GET',
            params=params or {},
        )
