import pytest
from lambdacalculus.bool import TRUE, FALSE 
from lambdacalculus.natural import ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN
from lambdacalculus.natural import decode_natural
from lambdacalculus.aritmetic import FAC, FIB, DIV, MOD, EVEN, ODD

@pytest.mark.parametrize("given, expected",[
  (ZERO, 1),
  (ONE, 1),
  (TWO ,2),
  (THREE, 6),
  (TEN, 2*3*4*5*6*7*8*9*10)
])
def test_fac(given, expected):
  assert decode_natural(FAC(given))==expected

@pytest.mark.parametrize("given, expected",[
  (ONE, 1),
  (TWO ,1),
  (THREE, 1+1),
  (FOUR, 1+2),
  (FIVE, 2+3)
])
def test_fib(given, expected):
  assert decode_natural(FIB(given))==expected

@pytest.mark.parametrize("left, right, expected",[
  (ONE, ONE , 1),
  (TWO ,ONE , 2),
  (FOUR, TWO, 2),
  (NINE, THREE, 3)
])
def test_div(left, right, expected):
  assert decode_natural(DIV(left)(right))==expected

@pytest.mark.parametrize("left, right, expected",[
  (ONE, ONE , 0),
  (TWO ,ONE , 0),
  (FOUR, TWO, 0),
  (NINE, THREE, 0),
  (TEN, THREE, 1),
  (NINE, FIVE, 4)
])
def test_mod(left, right, expected):
  assert decode_natural(MOD(left)(right))==expected

@pytest.mark.parametrize("given, expected",[
  (ONE, FALSE),
  (TWO ,TRUE),
  (THREE, FALSE),
  (FOUR, TRUE),
  (FIVE, FALSE)
])
def test_even(given, expected):
  assert EVEN(given) is expected
  assert ODD(given) is not expected


if __name__=="__main__":
  pytest(["-v"])
