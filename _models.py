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
        self.id: str = data['id']
        self.url: str = data['url']
        self.amount: int = data['amount']
        self.status: BILLING_STATUS = data['status']
        self.devMode: bool = data['devMode']
        self.methods: List[BILLING_METHODS] = data['methods']
        self.products: List[dict] = data['products']
        self.frequency: BILLING_KINDS = data['frequency']
        self.nextBilling: Union[str, None] = data.get('nextBilling')  # Optional field
        self.customer: Union[ICostumer, None] = data.get('customer')  # Optional field
        self.accountId: str = data['customerId']['accountId'] if 'customerId' in data else None
        self.storeId: str = data['customerId']['storeId'] if 'customerId' in data else None
        self.createdAt: str = data['createdAt']
        self.updatedAt: str = data['updatedAt']