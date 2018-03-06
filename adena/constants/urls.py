

class URL(object):
    BASE_URL = 'https://sandbox-approvals-api.getsimpl.com/api'
    VERSION = "/v2"
    PREV_VERSION = "/v1.1"
    SIMPL_USER_APPROVAL = "{}{}{}".format(BASE_URL, VERSION, "/simpl_buy/server/approved")
    SIMPL_CHARGE_TOKEN = "{}{}{}".format(BASE_URL, PREV_VERSION, "/transactions")