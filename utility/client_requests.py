import logging
import requests
import json

from adena.exceptions import ClientIdMissingException

logger = logging.getLogger(__name__)


class SimplUtility(object):
    """
        Utility class
    """

    def __init__(self, **kwargs):
        self._client_id = kwargs.get("client_id", None)
        if not self._client_id:
            raise ClientIdMissingException
        logger.debug("SimplUtility | initialized")


class RequestCaller(SimplUtility):
    """
     Utility to make http request calls
    """

    def __init__(self, **kwargs):
        super(RequestCaller, self).__init__(**kwargs)
        logger.debug("RequestCaller | initialized | client-id:{}".format(self._client_id))

    def post(self, url, payload=None, headers=None):
        logger.info("RequestCaller | post | payload:{}".format(payload))
        logger.info("RequestCaller | post | headers:{}".format(headers))
        logger.info("RequestCaller | post | url:{}".format(url))
        print("RequestCaller | post | payload:{}".format(payload))

        data = requests.post(url=url, headers=headers, data=json.dumps(payload))
        return data