import json

from adena.constants.urls import URL
from adena.resources.base import BaseResource


class Refund(BaseResource):

    def __init__(self, *args, **kwargs):
        super(Refund, self).__init__(kwargs)
        self.URL = URL(is_prod=self.client._is_prod)


    def make_refund(self, payload):
        """
        used to refund from simpl against the transaction-id for a particular order

        sample request, responses:
        :param    payload:
                {
                  "transaction_id": "21a5c7c4-9ead-480d-a288-f564142e0bac",
                  "amount_in_paise": 10000,
                  "reason": "failed to deliver on time"
                }
        :return:
                {
                  "success": true,
                  "data": {
                    "transaction_id": "21a5c7c4-9ead-480d-a288-f564142e0bac",
                    "refunded_transaction_id": "aa5e47e3-880f-4d24-8d16-38c0f3be3608"
                  },
                  "api_version": 1.1
                }
        """

        refund_url = self.URL.SIMPL_REFUND_TRANSACTION

        self.client.logger.debug("Refund | make_refund | payload:{}".format(payload))
        self.client.logger.debug("Refund | make_refund | charge_url:{}".format(refund_url))

        headers = {"authorization": self.client._client_secret}
        response = self.client.post(url=refund_url, headers=headers, payload=payload)

        self.client.logger.debug("Refund | make_refund | response:{}".format(json.loads(response.text)))

        return response