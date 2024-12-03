from typing import Literal

MINIMUM_VALUE = 100
BASEURL = "https://api.abacatepay.com/v1"
VERSION = "0.1.0"
USERAGENT = f"Python SDK {VERSION}"

BILLING_STATUS = Literal['PENDING', 'EXPIRED', 'CANCELLED', 'PAID', 'REFUNDED']
BILLING_METHODS = Literal['pix']
BILLING_KINDS = Literal['ONE_TIME']
