import pytest
from lambdacalculus.bool import NOR, NAND, XNOR, XOR, OR, AND, NOT, TRUE, FALSE 

@pytest.mark.parametrize("given, expected",[
  (TRUE,FALSE),
  (FALSE,TRUE)
])
def test_not(given, expected):
  assert NOT(given) is expected

@pytest.mark.parametrize("left, right, expected",[
  (TRUE, TRUE ,TRUE ),
  (TRUE, FALSE,FALSE),
  (FALSE,TRUE ,FALSE),
  (FALSE,FALSE,FALSE)
])
def test_and(left, right, expected):
  assert AND(left)(right) is expected

@pytest.mark.parametrize("left, right, expected",[
  (TRUE, TRUE ,TRUE ),
  (TRUE, FALSE,TRUE ),
  (FALSE,TRUE ,TRUE ),
  (FALSE,FALSE,FALSE)
])
def test_or(left, right, expected):
  assert OR(left)(right) is expected

@pytest.mark.parametrize("left, right, expected",[
  (TRUE, TRUE ,FALSE),
  (TRUE, FALSE,TRUE ),
  (FALSE,TRUE ,TRUE ),
  (FALSE,FALSE,FALSE)
])
def test_xor(left, right, expected):
  assert XOR(left)(right) is expected

@pytest.mark.parametrize("left, right, expected",[
  (TRUE, TRUE ,TRUE ),
  (TRUE, FALSE,FALSE),
  (FALSE,TRUE ,FALSE),
  (FALSE,FALSE,TRUE )
])
def test_xnor(left, right, expected):
  assert XNOR(left)(right) is expected

@pytest.mark.parametrize("left, right, expected",[
  (TRUE, TRUE ,FALSE),
  (TRUE, FALSE,TRUE ),
  (FALSE,TRUE ,TRUE ),
  (FALSE,FALSE,TRUE )
])
def test_nand(left, right, expected):
  assert NAND(left)(right) is expected

@pytest.mark.parametrize("left, right, expected",[
  (TRUE, TRUE ,FALSE),
  (TRUE, FALSE,FALSE),
  (FALSE,TRUE ,FALSE),
  (FALSE,FALSE,TRUE )
])
def test_nor(left, right, expected):
  assert NOR(left)(right) is expected

if __name__=="__main__":
  pytest(["-v"])
