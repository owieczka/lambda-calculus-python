import pytest
from lambdacalculus.bool import TRUE, FALSE 
from lambdacalculus.natural import ONE, THREE
from lambdacalculus.pair import CONS, CDR, CAR

@pytest.mark.parametrize("a, b",[
  (TRUE,FALSE),
  (FALSE,TRUE),
  (ONE, THREE)
])
def test_pair(a,b):
  pair = CONS(a)(b)
  assert CAR(pair) is a
  assert CDR(pair) is b

if __name__=="__main__":
  pytest(["-v"])
