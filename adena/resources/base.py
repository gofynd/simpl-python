

class BaseResource(object):

    def __init__(self, kwargs):
        self.client = kwargs.get("client")
        self.client.logger.debug("BaseResource | __init__ | called")
