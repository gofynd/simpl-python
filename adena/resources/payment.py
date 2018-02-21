from adena.constants.urls import URL
from adena.resources.base import BaseResource


class Payment(BaseResource):
    def __init__(self, client=None):
        super(Payment, self).__init__(client)

    def check_simpl_approval(self, payload):
        approval_url = URL.SIMPL_USER_APPROVAL

        self.logger.debug("Payment | check_simpl_approval | payload:{}".format(payload))
        print("Payment | check_simpl_approval | payload:{}".format(payload))
        self.logger.debug("Payment | check_simpl_approval | approval_url:{}".format(approval_url))
        print("Payment | check_simpl_approval | approval_url:{}".format(approval_url))

        headers = {"authorization": self.client._client_secret}
        response = self._request_caller.post(url=approval_url, headers=headers, payload=payload)

        self.logger.debug("Payment | check_simpl_approval | response:{}".format(response))
        print("Payment | check_simpl_approval | response:{}".format(response))

        return response