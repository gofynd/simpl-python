import simpl
import os
import unittest
import logging
import sys

# setting logger to print logs to stdout
# reference: https://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log
test_logger = logging.getLogger(__name__)
test_logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
test_logger.addHandler(ch)


def mock_file(filename):
    if not filename:
        return ''
    file_dir = os.path.dirname(__file__)
    file_path = "{}/mocks/{}.json".format(file_dir, filename)
    return open(file_path).read()


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = simpl.Client(client_secret="dcd0cad031b773aabaed11e23a5b43db", logger=test_logger)
        self.payment_id = 'fake_payment_id'
        self.refund_id = 'fake_refund_id'
        self.card_id = 'fake_card_id'
        self.customer_id = 'fake_customer_id'
        self.token_id = 'fake_token_id'
        self.addon_id = 'fake_addon_id'
        self.subscription_id = 'fake_subscription_id'
        self.plan_id = 'fake_plan_id'
        self.urls = simpl.URL(is_prod=self.client._is_prod)

        self.secondary_client = simpl.Client(client_secret="dcd0cad031b773aabaed11e23a5b43db")
