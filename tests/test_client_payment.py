
import responses
import json

from .helpers import mock_file, ClientTestCase

# run test as:
# python -m unittest discover

class TestClientPayment(ClientTestCase):

    def setUp(self):
        super(TestClientPayment, self).setUp()
        self.payload = {
                      "transaction_token": "2c88673bf945a41a527a01467a73150c", # generate and replace this token from client-side-sdk
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

    @responses.activate
    def test_charge(self):
        result = mock_file('make_charge')
        url = self.urls.SIMPL_CHARGE_TOKEN
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.charge_token(payload=self.payload).json(), result)
