from abacatepay import AbacatePay

def test_list_billings(list_billings_response):
    client = AbacatePay("dummy-token")
    billings = client.list_bills()
    assert len(billings) == 1
