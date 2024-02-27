import pytest
from lambdacalculus.natural import ZERO, ONE, TWO, THREE, FOUR, FIVE
from lambdacalculus.natural import decode_natural
from lambdacalculus.natural import SUCC, ADD, MUL, POW, PRED, SUB, DIFF
from lambdacalculus.natural import ISZERO, GTE, LTE, GT, LT, EQ
from lambdacalculus.natural import MIN, MAX
from lambdacalculus.bool import TRUE, FALSE

@pytest.mark.parametrize("given, expected",[
  (ZERO, 0),
  (ONE, 1),
  (TWO,2)
])
def test_decode_natural(given, expected):
  assert decode_natural(given) == expected

@pytest.mark.parametrize("given, expected",[
  (ZERO, 1),
  (ONE,  2),
  (TWO,  3)
])
def test_succ(given, expected):
  assert decode_natural(SUCC(given)) == expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ZERO, 0),
  (ZERO, ONE,  1),
  (ONE,  TWO,  3)
])
def test_add(left, right, expected):
  assert decode_natural(ADD(left)(right)) == expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ZERO, 0),
  (ZERO, ONE,  0),
  (ONE,  TWO,  2),
  (TWO,  TWO,  4)
])
def test_mul(left, right, expected):
  assert decode_natural(MUL(left)(right)) == expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ONE,   0),
  (ZERO, TWO,   0),
  (ONE,  TWO,   1),
  (TWO,  TWO,   4),
  (THREE,TWO,   9),
  (THREE,THREE, 27)
])
def test_pow(left, right, expected):
  assert decode_natural(POW(left)(right)) == expected

@pytest.mark.parametrize("given, expected",[
  (ZERO, 0),
  (ONE,  0),
  (TWO,  1),
  (THREE,2)
])
def test_pred(given, expected):
  assert decode_natural(PRED(given)) == expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ZERO, 0),
  (ZERO, ONE,  0),
  (ONE,  TWO,  0),
  (ONE, ZERO,  1),
  (TWO, ONE,   1)
])
def test_sub(left, right, expected):
  assert decode_natural(SUB(left)(right)) == expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ZERO, 0),
  (ZERO, ONE,  1),
  (ONE,  TWO,  1),
  (ONE, ZERO,  1),
  (TWO, ONE,   1),
  (TWO, ZERO,  2)
])
def test_diff(left, right, expected):
  assert decode_natural(DIFF(left)(right)) == expected

@pytest.mark.parametrize("given, expected",[
  (ZERO, TRUE),
  (ONE,  FALSE),
  (TWO,  FALSE),
  (THREE,FALSE)
])
def test_iszero(given, expected):
  assert ISZERO(given) is expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ZERO, TRUE),
  (ZERO, ONE,  FALSE),
  (ONE,  TWO,  FALSE),
  (ONE, ZERO,  TRUE),
  (TWO, ONE,   TRUE),
  (TWO, ZERO,  TRUE),
  (FIVE, TWO, TRUE)
])
def test_gte(left, right, expected):
  assert GTE(left)(right) is expected
  assert LT(left)(right) is not expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ZERO, TRUE),
  (ZERO, ONE,  TRUE),
  (ONE,  TWO,  TRUE),
  (ONE, ZERO,  FALSE),
  (TWO, ONE,   FALSE),
  (TWO, ZERO,  FALSE),
  (FIVE, TWO, FALSE)
])
def test_lte(left, right, expected):
  assert LTE(left)(right) is expected
  assert GT(left)(right) is not expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ZERO, TRUE),
  (ONE,  ONE,  TRUE),
  (ONE,  TWO,  FALSE),
  (ONE, ZERO,  FALSE),
  (TWO, ONE,   FALSE),
  (TWO, ZERO,  FALSE),
  (FIVE, FIVE, TRUE)
])
def test_eq(left, right, expected):
  assert EQ(left)(right) is expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ZERO, ZERO),
  (ONE,  ONE,  ONE),
  (ONE,  TWO,  TWO),
  (ONE, ZERO,  ONE),
  (TWO, ONE,   TWO),
  (TWO, ZERO,  TWO),
  (FIVE, THREE, FIVE)
])
def test_max(left, right, expected):
  assert MAX(left)(right) is expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ZERO, ZERO),
  (ONE,  ONE,  ONE),
  (ONE,  TWO,  ONE),
  (ONE, ZERO,  ZERO),
  (TWO, ONE,   ONE),
  (TWO, ZERO,  ZERO),
  (FIVE, THREE, THREE)
])
def test_min(left, right, expected):
  assert MIN(left)(right) is expected
  
  
if __name__=="__main__":
  pytest(["-v"])
