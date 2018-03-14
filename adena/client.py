import logging
import requests
import json

from types import ModuleType

from adena.custom_logging import MyLogger

logging.setLoggerClass(MyLogger)
logging.basicConfig()
global_logger = logging.getLogger(__name__)

from adena.exceptions import ClientSecretMissingException

from . import resources, utility

def capitalize_camel_case(string):
    return "".join(map(str.capitalize, string.split('_')))


# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and \
            capitalize_camel_case(name) in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[capitalize_camel_case(name)]

UTILITY_CLASSES = {}
for name, module in utility.__dict__.items():
    if isinstance(module, ModuleType) and name.capitalize() in module.__dict__:
        UTILITY_CLASSES[name] = module.__dict__[name.capitalize()]

class Client(object):
    """Adena client class"""

    def __init__(self, **options):
        self._client_secret = options.get("client_secret", None)
        self._is_debug = options.get("is_debug", None)
        self._is_prod = options.get("is_prod", None)

        logger = options.get("logger", None)
        self.logger = logger
        if not logger:
            self.logger = global_logger

        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(**{"client": self}))

        for name, Klass in UTILITY_CLASSES.items():
            setattr(self, name, Klass(**{"client": self}))

        if not self._client_secret:
            raise ClientSecretMissingException

    def post(self, url, payload=None, headers=None):
        self.logger.info("Client | post | payload:{}".format(payload))
        self.logger.info("Client | post | headers:{}".format(headers))
        self.logger.info("Client | post | url:{}".format(url))

        content_type = headers.get("content-type", None)
        if not content_type:
            headers["content-type"] = "application/json"
        response = requests.post(url=url, headers=headers, data=json.dumps(payload))

        # changed as per simpl python code scippet
        # reference: https://sandbox.getsimpl.com/docs/web/custom#step-final-charge-transaction-token (check python-code sample)
        # domain = URL.DOMAIN_URL
        # if self.is_approval_flow:
        #     domain = URL.APPROVAL_DOMAIN_URL
        # conn = http.client.HTTPSConnection(domain)
        # conn.request("POST", "{}{}{}".format(URL.MIDDLEWARE, URL.PREV_VERSION, URL.SIMPL_CHARGE_TOKEN), payload, headers)
        # res = conn.getresponse()
        # data = res.read()
        # response = data.decode("utf-8")

        self.logger.info("Client | post | response:{}".format(response))
        return response