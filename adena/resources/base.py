from adena.client import Client
from adena.custom_logging import MyLogger
from utility.client_requests import RequestCaller
import logging

logging.setLoggerClass(MyLogger)
logging.basicConfig()
logger = logging.getLogger(__name__)

class BaseResource:

    def __init__(self, **kwargs):
        self._client = Client(**kwargs)
        self._request_caller = RequestCaller(client_id=self._client._client_secret, logger=logger)
        self.logger = logger

        self.logger.debug("BaseResource | __init__ | called")
        print("BaseResource | __init__ | called")
