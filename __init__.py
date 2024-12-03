from .src.billing import Billing
from typing import Literal
from ._models import Product, IBilling
from ._constants import BILLING_KINDS, BILLING_METHODS, BASEURL, USERAGENT
import requests

class AbacatePay:
  """
  The AbacatePay sdk client.
  """

  def __init__(self, api_key: str):
    self.api_key = api_key

  def request(self, url: str, method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"] = "GET", **kwargs):
    return requests.request(method, url,  headers={"Authorization": f"Bearer {self.api_key}", "User-Agent": USERAGENT}, **kwargs)

  def CreateBilling(self, products:list[Product], returnURL:str, completionUrl:str, methods:list[BILLING_METHODS]=['PIX'], frequency:BILLING_KINDS='ONE_TIME'):
    return Billing(products, returnURL, completionUrl, self.api_key, methods, frequency=frequency)

  def listBills(self) -> list[IBilling]:
    data = self.request(f"{BASEURL}/billing/list", method="GET").json()
    return [IBilling(data=bill) for bill in data['billings']]