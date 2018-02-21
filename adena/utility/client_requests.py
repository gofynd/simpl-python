import requests
import json
import logging

logger = logging.getLogger(__name__)


class SimplUtility(object):

    """
        Utility class
    """

    def __init__(self, **kwargs):
        self._client_id = kwargs.get("client_id", None)
        self.logger = kwargs.get("logger")
        self.logger.debug("SimplUtility | initialized")


class RequestCaller(SimplUtility):
    """
     Utility to make http request calls
    """

    def __init__(self, **kwargs):
        super(RequestCaller, self).__init__(**kwargs)
        self.logger.debug("RequestCaller | initialized | client-id:{}".format(self._client_id))

    def post(self, url, payload=None, headers=None):
        self.logger.info("RequestCaller | post | payload:{}".format(payload))
        self.logger.info("RequestCaller | post | headers:{}".format(headers))
        self.logger.info("RequestCaller | post | url:{}".format(url))
        print("RequestCaller | post | payload:{}".format(payload))

        response = requests.post(url=url, headers=headers, data=json.dumps(payload))

        self.logger.info("RequestCaller | post | response:{}".format(response))
        print("RequestCaller | post | response:{}".format(response))
        return response