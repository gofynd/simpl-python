
import responses
import json

from .helpers import mock_file, ClientTestCase

# run test as:
# python -m unittest discover

class TestClientRefund(ClientTestCase):

    def setUp(self):
        super(TestClientRefund, self).setUp()
        self.payload = {
                          "transaction_id": "18CF6118-AD0A-4F9B-BD41-5C8A3C42FCE7",
                          "amount_in_paise": 100000,
                          "reason": "failed to deliver on time"
                        }

    @responses.activate
    def test_charge(self):
        result = mock_file('make_refund')
        url = self.urls.SIMPL_REFUND_TRANSACTION
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.refund.make_refund(payload=self.payload).json(), result)
