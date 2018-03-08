import http.client
import json

from adena import URL

conn = http.client.HTTPSConnection(URL.DOMAIN_URL)

req_param = {
  'transaction_token': 'ad9ac63046f493b9f99ad56051ce9b94',
  'amount_in_paise': 100000,
  'order_id': 'ABC126',
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

payload = json.dumps(req_param)

headers = {
    'authorization': "dcd0cad031b773aabaed11e23a5b43db",
    'content-type': "application/json"
    }

# conn.request("POST", "/api/v1.1/transactions", payload, headers)
conn.request("POST", "{}{}{}".format(URL.MIDDLEWARE, URL.PREV_VERSION, URL.SIMPL_CHARGE_TOKEN_ENDPOINT), payload, headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))