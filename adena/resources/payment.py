import json

from adena.constants.urls import URL
from adena.resources.base import BaseResource


class Payment(BaseResource):

    def __init__(self, *args, **kwargs):
        super(Payment, self).__init__(kwargs)

    def charge_token(self, payload):
        """
        used to charge simpl against the token for a particular order

        sample request, responses:
        :param    payload:
                {
                      "transaction_token": "2c88673bf945a41a527a01467a73150c",
                      "amount_in_paise": 100000,
                      "order_id": "ABC123",
                      "items": [{
                        "sku": "123123123",
                        "quantity": 2,
                        "unit_price_in_paise": 10000,
                        "display_name": "apples"
                        },
                        {
                          "sku": "123123124",
                          "quantity": 1,
                          "unit_price_in_paise": 10000,
                          "display_name": "oranges"
                        }],
                      "shipping_address": {
                        "line1": "Shipping line1",
                        "line2": "Shipping line2",
                        "city": "Mumbai",
                        "state": "Maharastra",
                        "pincode": "400072"
                      },
                      "billing_address": {
                        "line1": "Shipping line1",
                        "line2": "Shipping line2",
                        "city": "Mumbai",
                        "state": "Maharastra",
                        "pincode":"400072"
                        },
                      "shipping_amount_in_paise": 1000,
                      "discount_in_paise": 0,
                      "metadata":[
                        {"key1": "value"},
                        {"key1": "value"}
                      ]
                }
        :return:
                {
                  "success": true,
                  "data": {
                    "transaction": {
                      "transaction_id": "d6ab8299-572b-445d-a717-6c6ecd5f5d39",
                      "items": [
                        {
                          "sku": "123123123",
                          "quantity": 2,
                          "unit_price_in_paise": 10000,
                          "display_name": "apples"
                        },
                        {
                          "sku": "123123124",
                          "quantity": 1,
                          "unit_price_in_paise": 10000,
                          "display_name": "oranges"
                        }
                      ],
                      "amount_in_paise": 100000,
                      "delivered": false,
                      "shipping_amount_in_paise": 1000,
                      "discount_in_paise": 0,
                      "billing_address": {
                        "line1": "Shipping line1",
                        "line2": "Shipping line2",
                        "city": "Mumbai",
                        "state": "Maharastra",
                        "pincode": "400072"
                      },
                      "shipping_address": {
                        "line1": "Shipping line1",
                        "line2": "Shipping line2",
                        "city": "Mumbai",
                        "state": "Maharastra",
                        "pincode": "400072"
                      },
                      "metadata": [
                        {
                          "key1": "value"
                        },
                        {
                          "key1": "value"
                        }
                      ],
                      "created_at": "2018-03-05T08:48:35.364Z",
                      "status": "CLAIMED"
                    },
                    "messages": [
                      "Your transaction was successfully updated"
                    ]
                  },
                  "api_version": 1
                }
        """

        charge_url = URL.SIMPL_CHARGE_TOKEN

        self.client.logger.debug("Payment | charge_token | payload:{}".format(payload))
        self.client.logger.debug("Payment | charge_token | charge_url:{}".format(charge_url))

        headers = {"authorization": self.client._client_secret}
        response = self.client.post(url=charge_url, headers=headers, payload=payload)

        self.client.logger.debug("Payment | charge_token | response:{}".format(json.loads(response.text)))

        return response