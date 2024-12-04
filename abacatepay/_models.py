from typing import List, Optional, Union, Literal
from ._constants import BILLING_STATUS, BILLING_METHODS, BILLING_KINDS
from pydantic import BaseModel

class Product(BaseModel):
  externalId: str
  name: str
  quantity: int
  price: int
  description: str

class Customer(BaseModel):
    taxId: str
    name: str
    email: str
    cellphone: str

class ICostumer:
    def __init__(self, data:dict):
        self.data = data
        self.formatJson(data)

    def formatJson(self, data:dict):
        self.id = data['id']
        self.taxId: str = data['metadata']['taxId']
        self.name: str = data['metadata']['name']
        self.email: str = data['metadata']['email']
        self.cellphone: str = data['metadata']['cellphone']

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
        self.customer: Union[ICostumer, None] = ICostumer(data=billingData.get('customer')) if 'customer' in billingData else None  # Optional field
        self.accountId: str = billingData['customerId']['accountId'] if 'customerId' in billingData else None
        self.storeId: str = billingData['customerId']['storeId'] if 'customerId' in billingData else None
        self.createdAt: str = billingData['createdAt']
        self.updatedAt: str = billingData['updatedAt']

