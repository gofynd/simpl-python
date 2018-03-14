

class SimplUtility(object):

    """
        Utility Base class
    """

    def __init__(self, **kwargs):
        self._client_id = kwargs.get("client_id", None)
        self.logger = kwargs.get("logger")
        self.logger.debug("SimplUtility | initialized")