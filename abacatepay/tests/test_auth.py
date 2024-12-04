import abacatepay
import abacatepay._exceptions



def test_WrongKey_RunningFunction():
  rightKey = "Bearer 123456789"
  try:
    client = abacatepay.AbacatePay(rightKey)
    ErrObj = client
    client.listBills()
  except Exception as e:
    ErrObj = e
  assert type(ErrObj) == abacatepay._exceptions.ForbiddenRequest