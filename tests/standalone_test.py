import json

import requests

from simpl.constants.urls import URL

url = "{}{}{}{}{}".format(URL.HTTPS_URL, URL.DOMAIN_URL, URL.MIDDLEWARE, URL.PREV_VERSION, URL.SIMPL_CHARGE_TOKEN_ENDPOINT)
print(url)

headers = {"authorization": "dcd0cad031b773aabaed11e23a5b43db", 'content-type': "application/json"}

payload = {
  'transaction_token': '450cd1d3974e2a35c740b78131cb297c',
  'amount_in_paise': 100000,
  'order_id': 'ABC127',
  'items': [
    {
      'sku': '123123123',
      'quantity': 2,
      'unit_price_in_paise': 10000,
      'display_name': 'apples'
    },
    {
      'sku': '123123124',
      'quantity': 1,
      'unit_price_in_paise': 10000,
      'display_name': 'oranges'
    }
  ],
  'shipping_address': {
    'line1': 'Shipping line1',
    'line2': 'Shipping line2',
    'city': 'Mumbai',
    'state': 'Maharastra',
    'pincode': '400072'
  },
  'billing_address': {
    'line1': 'Shipping line1',
    'line2': 'Shipping line2',
    'city': 'Mumbai',
    'state': 'Maharastra',
    'pincode': '400072'
  },
  'shipping_amount_in_paise': 1000,
  'discount_in_paise': 0,
  'metadata': [
    {
      'key1': 'value'
    },
    {
      'key1': 'value'
    }
  ]
}

response = requests.post(url=url, headers=headers, data=json.dumps(payload))

print(response.text)