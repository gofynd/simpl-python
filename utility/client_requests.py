import logging
import requests

from adena.exceptions import ClientIdMissingException

logger = logging.getLogger(__name__)

class SimplUtility:
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
        super.__init__(**kwargs)
        logger.debug("RequestCaller | initialized | client-id:{}".format(self._client_id))

    def get(self, url, payload=None, headers=None):
        logger.info("RequestCaller | get | payload:{}".format(payload))
        logger.info("RequestCaller | get | headers:{}".format(headers))
        logger.info("RequestCaller | get | url:{}".format(url))

        data = requests.get(url=url, headers=headers, params=payload)
        return data