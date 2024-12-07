from typing import List, Union
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


class Costumer:
    def __init__(self, data: dict):
        self.data = data
        self._format_json(data)

    def _format_json(self, data: dict):
        self.id = data["id"]
        self.taxId: str = data["metadata"]["taxId"]
        self.name: str = data["metadata"]["name"]
        self.email: str = data["metadata"]["email"]
        self.cellphone: str = data["metadata"]["cellphone"]


class Billing:
    def __init__(self, data: dict):
        self.data = data
        self._format_json(data)

    def _format_json(self, data: dict):
        billing_data = data

        self.id: str = billing_data["id"]
        self.url: str = billing_data["url"]
        self.amount: int = billing_data["amount"]
        self.status: BILLING_STATUS = billing_data["status"]
        self.dev_mode: bool = billing_data["devMode"]
        self.methods: List[BILLING_METHODS] = billing_data["methods"]
        self.products: List[dict] = billing_data["products"]
        self.frequency: BILLING_KINDS = billing_data["frequency"]
        self.next_billing: Union[str, None] = billing_data.get(
            "nextBilling"
        )  # Optional field
        self.customer: Union[Costumer, None] = (
            Costumer(data=billing_data.get("customer"))
            if "customer" in billing_data
            else None
        )  # Optional field
        self.account_id: str = (
            billing_data["customerId"]["accountId"]
            if "customerId" in billing_data
            else None
        )
        self.store_id: str = (
            billing_data["customerId"]["storeId"]
            if "customerId" in billing_data
            else None
        )
        self.created_at: str = billing_data.get("createdAt")
        self.updated_at: str = billing_data.get("updatedAt")
