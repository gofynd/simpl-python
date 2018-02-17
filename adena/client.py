
import logging

from adena.constants.urls import URL
from utility.client_requests import RequestCaller


logger = logging.getLogger(__name__)


class Client:
    """Adena client class"""

    DEFAULTS = {
        'base_url': URL.BASE_URL + URL.VERSION
    }

    def __init__(self, client_secret, is_debug=False, is_prod=False, **options):
        self._client_secret = client_secret
        self._is_debug = is_debug
        self._is_prod = is_prod
        self._request_caller = RequestCaller(client_id=self._client_secret)


    def check_simpl_approval(self, payload):
        approval_url = "{}{}".format(self.DEFAULTS["base_url"],URL.SIMPL_USER_APPROVAL)
        logger.debug("Client | check_simpl_approval | approval_url:{}".format(approval_url))

        headers = {"authorization": self._client_secret}
        response =  self._request_caller.get(url=approval_url, headers=headers)

        logger.debug("Client | check_simpl_approval | response:{}".format(response))
        return response

