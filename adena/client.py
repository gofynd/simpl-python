import logging

from types import ModuleType

logger = logging.getLogger(__name__)
from adena.exceptions import ClientIdMissingException

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
        self._client_secret = options.get("client_secret", None)

        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

        for name, Klass in UTILITY_CLASSES.items():
            setattr(self, name, Klass(self))

        if not self._client_secret:
            raise ClientIdMissingException