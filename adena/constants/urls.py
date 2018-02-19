

class URL(object):
    BASE_URL = 'https://sandbox-approvals-api.getsimpl.com/api'
    VERSION = "/v2"
    SIMPL_USER_APPROVAL = "{}{}{}".format(BASE_URL, VERSION, "/simpl_buy/server/approved")