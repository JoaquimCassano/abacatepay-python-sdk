import pytest

@pytest.fixture
def invalid_token_response(responses):
    responses.add(
        responses.GET,
        "https://api.abacatepay.com/v1/billing/list",
        status=401,
    )
    return responses

@pytest.fixture
def list_billings_response(responses):
    responses.add(
        responses.GET,
        "https://api.abacatepay.com/v1/billing/list",
        json={
            "data": [
                {
                    "id": "bill-5678",
                    "url": "https://pay.abacatepay.com/bill-5678",
                    "amount": 4000,
                    "status": "PENDING",
                    "devMode": True,
                    "methods": ["PIX"],
                    "products": [{"productId": "prod-1234", "quantity": 2}],
                    "frequency": "ONE_TIME",
                    "nextBilling": None,
                    "customer": {
                        "id": "cust-9876",
                        "metadata": {
                            "name": "João da Silva",
                            "cellphone": "+5511999999999",
                            "email": "joao.silva@example.com",
                            "taxId": "123.456.789-00",
                        },
                    },
                }
            ]
        },
        status=200,
    )
    return responses
