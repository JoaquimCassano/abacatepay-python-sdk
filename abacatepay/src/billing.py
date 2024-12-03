import requests
from .._constants import BASEURL, USERAGENT, BILLING_KINDS, BILLING_METHODS, BILLING_STATUS
from .._exceptions import *
from .._models import Product, IBilling
from typing import Literal

class Billing:
  def __init__(self, products:list[Product], returnURL:str, completionUrl:str, api_key:str, methods:list[BILLING_METHODS]=['PIX'], frequency:BILLING_KINDS='ONE_TIME'):
    self.products = products
    self.returnURL = returnURL
    self.completionUrl = completionUrl
    self.methods = methods
    print([product.model_dump() for product in products])
    response = requests.post(
      f"{BASEURL}/billing/create",
      json={
        "products": [product.model_dump() for product in products],
        "returnUrl": returnURL,
        "completionUrl": completionUrl,
        "methods": methods,
        "frequency": frequency
      },
      headers={
        "Authorization": f"Bearer {api_key}",
        "User-Agent": USERAGENT,
        "Content-Type": "application/json"
      }
    )

    try:
        if response.status_code == 200:
            billing_data = IBilling(data=response.json()['billing'])
            self.data = billing_data
        else:
            raise_for_status(response)
    except requests.exceptions.Timeout:
        raise APITimeoutError(request=response)
    except requests.exceptions.ConnectionError:
        raise APIConnectionError(message="Connection error.", request=response)

