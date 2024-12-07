# AbacatePay
Python sdk to interact with abacatepay's api


## Usage/Examples

```python
import abacatepay

token = "<your enviroment api token>"
client = AbacatePay(token)

billing = client.CreateBilling(products=[Product(externalId="123", name="Teste", quantity=1, price=101, description="Teste")], returnURL="https://abacatepay.com", completionUrl="https://abacatepay.com")
print(billing.data.url)
# > https://abacatepay.com/pay/aaaaaaa
```
