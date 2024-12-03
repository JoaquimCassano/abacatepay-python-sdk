from typing import List, Optional, Union, Literal
from ._constants import BILLING_STATUS, BILLING_METHODS, BILLING_KINDS
from pydantic import BaseModel

class Product(BaseModel):
  externalId: str
  name: str
  quantity: int
  price: int
  description: str



class ICostumer:
    def __init__(self, data:dict):
        self.data = data
        self.formatJson(data)

    def formatJson(self, data:dict):
        self.taxId: str = data['id']
        self.name: str = data['name']
        self.email: str = data['email']
        self.cellphone: str = data['phone']

class IBilling:
    def __init__(self, data:dict):
        self.data = data
        self.formatJson(data)

    def formatJson(self, data: dict):
        billingData = data

        self.id: str = billingData['publicId']
        self.url: str = billingData['url']
        self.amount: int = billingData['amount']
        self.status: BILLING_STATUS = billingData['status']
        self.devMode: bool = billingData['devMode']
        self.methods: List[BILLING_METHODS] = billingData['methods']
        self.products: List[dict] = billingData['products']
        self.frequency: BILLING_KINDS = billingData['frequency']
        self.nextBilling: Union[str, None] = billingData.get('nextBilling')  # Optional field
        self.customer: Union[ICostumer, None] = billingData.get('customer')  # Optional field
        self.accountId: str = billingData['customerId']['accountId'] if 'customerId' in billingData else None
        self.storeId: str = billingData['customerId']['storeId'] if 'customerId' in billingData else None
        self.createdAt: str = billingData['createdAt']
        self.updatedAt: str = billingData['updatedAt']

