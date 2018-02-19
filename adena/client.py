from adena.exceptions import ClientIdMissingException


class Client:
    """Adena client class"""

    def __init__(self, **options):
        self._client_secret = options.get("client_secret", None)
        self._is_debug = options.get("is_debug", None)
        self._is_prod = options.get("is_prod", None)
        self._client_secret = options.get("client_secret", None)

        if not self._client_secret:
            raise ClientIdMissingException