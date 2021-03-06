import json

from simpl.constants.urls import URL
from simpl.resources.base import BaseResource


class Approval(BaseResource):

    def __init__(self, *args, **kwargs):
        super(Approval, self).__init__(kwargs)
        self.URL = URL(is_prod=self.client._is_prod)

    def check_simpl_approval(self, payload):
        """
        to check whether this user is allowed to use simpl

        sample request, responses:
        :param    payload: {
                            "payload": "vvuIoU47qnwlgOktO6HVeVIbC63X0hcenzKVU/o6NJWgpE+UVQrtGiC4+pLfeD9K9+0EfGJHFXEkJSpPVKSkoJKG5p2K9cQRsBzj5rvXQqyhHQ2YJ6N7piAdfoPa8K8E8pX/4tan8yETgk/2nkmmdUexyzxrGQIBxYwYctup+QSeALA8YX9GuSCIpJbMwop8p8NSDWQ+jfqUu/u5C+N8UVti1/LXgEJmXM3XBbvuyHq3TT6mUbq7XgzorGp8jnNzJZ57PICaVB/K5F4xGYqP6yQ0STKh53Hr+mndGJ86p2PltWYUdNylXLD+ta+3vm3j3Bjy0smEK0D9/ehidmos/IuCRZcwlD4RCtI1cE9buI1vcRadoV9MGK2tramaht0rtt2h8GyUETdHA/esDYRHYVEr8Sh11LPl9PGEfEy4d2QXft0bZ1GscIsb05kDnIM6b0iyX4P/IsXnz2rrJgvfI+lJIdt3CFAMzxGXbvgOdbKspVNvv/ggJcXa3/PiGmaSgOzhXRoP2TlV5BFm0pUlPqUM9NnMeNjMozqtCxcc3sZl4IkYaMb0Ntrv8bKCdYO6S52OobdAAt8WjVZ8mPTEV+v8KY00rCmmTL1FzlWkHhI2pMfC8518WuLdwmaLRu1yLBI4/HKsx98vL6Q35ifJTQmDjSQEbLENl6WAUQ6fDUyQm8WZ5VqcAD012T/d1/grRRSP7eZNLSk6A0YEXbbY0Ox5xp0xSFtZClwYUOqUMb3s/Rf/7/7dggSKB+nBAtT2gTvbdzcgOTD3xHhU1Cizqig4dW8FpOj5B+TMYPZ0mgiBDG4cNpfPD4JF6ONBzaoKsQCoOGgfKZV2h+j62yUsCfHnq8ZCDT+rCsPYJbS/8PAWEds+zUfUS8bVqpvJYsTB1fsv7Dva8oo13k9FNdfLMO2IOTgCa0Poi0ULFODVg2jhTD8nvrIOCbJxu+jKTYNYwFT39i/TxJLYpJDzm0Yc8/CDwM37+tRbjJzmDddvFyEpu0YLQBVDmLlnU2miqx7NH/Aq7crRoWd8SFaT+bfEeiXyq+ZAfXlhyugeHNO37SMwZo10bSbpvHjUbb5+8r1yH7dAASRnGYhW0j8M/OVqyPBa8DgCSBcZCTQ3np0YBcdSTG7hcDCTjOXOxDxD9Kq9zZ385Gc21fwAB/2I2kQd+ItOrDDyREeUtAtdAegKJkptdLHXRMDGv4RvtPa2pt+Q/2qQxt+oKMAyEglE2sl6WOtveDTZmh+gcXLRQ4tXwYCX4rbiB5xsDqS9zucZgWNvXxnVLSS2X4NVEFIg7y3XcGnR0yFBf4O44bbH0b1jYwZKtzjPbc2Ne8POu8sQNlkti1Yz9JOzy9ToBpq4pNBmhHlZMN5R3pz6yoZiSk9LcFPeS9Pl8iO3I+p5D+4myTkg+SMWLd/7sxTQcEzqnDk0+kCyPzR5YcfCRdRsS3gyARbacrPIwE75HtAsCKeran08",
                            "phone_number": "9029198999",
                            "transaction_amount_in_paise": 10000,
                            "merchant_params": {
                                "order-id": "UYUWYJ-232h3h",
                                "restaurant-address": "80 ft road, Indiranangar",
                                "delivery-lt-ln": "12.9748295, 77.6469903"
                            }
                        }
        :return: "data": {
                        "api_version": 2,
                        "data": {
                            "approved": true,
                            "button_text": "Buy Now, Pay Later",
                            "first_transaction": false
                        },
                        "success": true
                    }
        """

        approval_url = self.URL.SIMPL_USER_APPROVAL

        self.client.logger.debug("Approval | check_simpl_approval | payload:{}".format(payload))
        self.client.logger.debug("Approval | check_simpl_approval | approval_url:{}".format(approval_url))

        headers = {"authorization": self.client._client_secret}
        response = self.client.post(url=approval_url, headers=headers, payload=payload)

        self.client.logger.debug("Approval | check_simpl_approval | response:{}".format(json.loads(response.text)))

        return response
