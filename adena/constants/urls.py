

class URL(object):

    APPROVAL_DOMAIN_URL = 'sandbox-approvals-api.getsimpl.com'
    DOMAIN_URL = "sandbox-api.getsimpl.com"
    HTTPS_URL = "https://"
    MIDDLEWARE = "/api"
    APPROVAL_BASE_URL = "{}{}{}".format(HTTPS_URL, APPROVAL_DOMAIN_URL, MIDDLEWARE)
    BASE_URL = "{}{}{}".format(HTTPS_URL, DOMAIN_URL, MIDDLEWARE)
    VERSION = "/v2"
    PREV_VERSION = "/v1.1"
    SIMPL_USER_APPROVAL = "{}{}{}".format(APPROVAL_BASE_URL, VERSION, "/simpl_buy/server/approved")
    SIMPL_CHARGE_TOKEN_ENDPOINT = "/transactions"
    SIMPL_CHARGE_TOKEN = "{}{}{}".format(BASE_URL, PREV_VERSION, SIMPL_CHARGE_TOKEN_ENDPOINT)

    def __init__(self, is_prod):
        self.is_prod = is_prod
        if self.is_prod:
            # change this to PROD urls in PRODUCTION
            self.APPROVAL_DOMAIN_URL = ''
            self.DOMAIN_URL = ""