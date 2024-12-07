"""
The python SDK for the AbacatePay API

Basic usage:
```python
import abacatepay

token = "<your api token>"
client = AbacatePay(token)

billing = x = client.CreateBilling(products=[Product(externalId="123", name="Teste", quantity=1, price=101, description="Teste")], returnURL="https://abacatepay.com", completionUrl="https://abacatepay.com")
print(billing.data.url)
# > https://abacatepay.com/pay/aaaaaaa
```

More examples found on https://abacatepay.readme.io/
"""


from .src.billing import Billing
from typing import Literal
from ._models import Product, IBilling, Customer
from ._constants import BILLING_KINDS, BILLING_METHODS, BASEURL, USERAGENT
from ._exceptions import *
import requests

class AbacatePay:
  """
  The AbacatePay sdk client.
  """

  def __init__(self, api_key: str):
    self.__api_key = api_key

  def request(self, url: str, method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"] = "GET", **kwargs):
    return requests.request(method, url,  headers={"Authorization": f"Bearer {self.__api_key}", "User-Agent": USERAGENT}, **kwargs)

  def CreateBilling(self, products:list[Product], returnURL:str, completionUrl:str, methods:list[BILLING_METHODS]=['PIX'], frequency:BILLING_KINDS='ONE_TIME', customerId:str|None=None, customer:Customer|None=None):
    return Billing(products, returnURL, completionUrl, self.__api_key, methods, frequency=frequency, customerId=customerId, customer=customer)

  def listBills(self) -> list[IBilling]:
    response = self.request(f"{BASEURL}/billing/list", method="GET")
    try:
        if response.status_code == 200:
            return [IBilling(data=bill) for bill in response.json()['data']]
        else:
            raise_for_status(response)
    except requests.exceptions.Timeout:
        raise APITimeoutError(request=response)
    except requests.exceptions.ConnectionError:
        raise APIConnectionError(message="Connection error.", request=response)

