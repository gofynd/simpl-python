from adena.custom_logging import MyLogger
from adena.utility.client_requests import RequestCaller
import logging

logging.setLoggerClass(MyLogger)
logging.basicConfig()
logger = logging.getLogger(__name__)


class BaseResource(object):

    def __init__(self, client=None):
        self.client = client
        self._request_caller = RequestCaller(client_id=self.client._client_secret, logger=logger)
        self.logger = logger

        self.logger.debug("BaseResource | __init__ | called")
        print("BaseResource | __init__ | called")
