import pytest
from lambdacalculus.natural import ZERO, ONE, TWO, THREE, FOUR, FIVE
from lambdacalculus.signed import SIGNED
from lambdacalculus.signed import decode_signed
from lambdacalculus.signed import SADD, SMUL, SSUB
#from lambdacalculus.natural import ISZERO, GTE, LTE, GT, LT, EQ
#from lambdacalculus.natural import MIN, MAX
from lambdacalculus.bool import TRUE, FALSE

@pytest.mark.parametrize("sign, given, expected",[
  (TRUE, ZERO, 0),
  (TRUE, ONE, 1),
  (TRUE, TWO, 2),
  (FALSE, ZERO, -0),
  (FALSE, ONE, -1),
  (FALSE, TWO, -2)
])
def test_signed(sign, given, expected):
  assert decode_signed(SIGNED(sign)(given)) == expected

@pytest.mark.parametrize("leftsign, left, rightsign, right, expected",[
  (TRUE, ZERO, TRUE, ZERO, 0),
  (TRUE, ZERO, TRUE, ONE,  1),
  (TRUE, ONE,  TRUE, TWO,  3),
  (TRUE, THREE, FALSE, ONE,  2),
  (FALSE, ONE,  TRUE, TWO,  1),
  (TRUE, ONE, FALSE, THREE,  -2),
  (FALSE, THREE, TRUE, ONE,  -2),
  (FALSE, THREE, FALSE, ONE,  -4),
])
def test_sadd(leftsign, left, rightsign, right, expected):
  assert decode_signed(SADD(SIGNED(leftsign)(left))(SIGNED(rightsign)(right))) == expected

@pytest.mark.parametrize("leftsign, left, rightsign, right, expected",[
  (TRUE, ZERO, TRUE, ZERO, 0),
  (TRUE, ZERO, TRUE, ONE,  -1),
  (TRUE, ONE,  TRUE, TWO,  -1),
  (TRUE, THREE, FALSE, ONE,  4),
  (FALSE, ONE,  TRUE, TWO,  -3),
  (TRUE, ONE, FALSE, THREE,  4),
  (FALSE, THREE, TRUE, ONE,  -4),
  (FALSE, THREE, FALSE, ONE,  -2),
])
def test_ssub(leftsign, left, rightsign, right, expected):
  assert decode_signed(SSUB(SIGNED(leftsign)(left))(SIGNED(rightsign)(right))) == expected

@pytest.mark.parametrize("leftsign, left, rightsign, right, expected",[
  (TRUE, ZERO, TRUE, ZERO, 0),
  (TRUE, ZERO, TRUE, ONE,  0),
  (TRUE, ONE,  TRUE, TWO,  2),
  (TRUE, THREE, FALSE, ONE, -3),
  (FALSE, ONE,  TRUE, TWO,  -2),
  (TRUE, ONE, FALSE, THREE,  -3),
  (FALSE, THREE, TRUE, ONE,  -3),
  (FALSE, THREE, FALSE, ONE,  3),
])
def test_smul(leftsign, left, rightsign, right, expected):
  assert decode_signed(SMUL(SIGNED(leftsign)(left))(SIGNED(rightsign)(right))) == expected


#@pytest.mark.parametrize("given, expected",[
#  (ZERO, TRUE),
#  (ONE,  FALSE),
#  (TWO,  FALSE),
#  (THREE,FALSE)
#])
#def test_iszero(given, expected):
#  assert ISZERO(given) is expected

#@pytest.mark.parametrize("left, right, expected",[
#  (ZERO, ZERO, TRUE),
#  (ZERO, ONE,  FALSE),
#  (ONE,  TWO,  FALSE),
#  (ONE, ZERO,  TRUE),
#  (TWO, ONE,   TRUE),
#  (TWO, ZERO,  TRUE),
#  (FIVE, TWO, TRUE)
#])
#def test_gte(left, right, expected):
#  assert GTE(left)(right) is expected
#  assert LT(left)(right) is not expected

#@pytest.mark.parametrize("left, right, expected",[
#  (ZERO, ZERO, TRUE),
#  (ZERO, ONE,  TRUE),
#  (ONE,  TWO,  TRUE),
#  (ONE, ZERO,  FALSE),
#  (TWO, ONE,   FALSE),
#  (TWO, ZERO,  FALSE),
#  (FIVE, TWO, FALSE)
#])
#def test_lte(left, right, expected):
#  assert LTE(left)(right) is expected
#  assert GT(left)(right) is not expected

#@pytest.mark.parametrize("left, right, expected",[
#  (ZERO, ZERO, TRUE),
#  (ONE,  ONE,  TRUE),
#  (ONE,  TWO,  FALSE),
#  (ONE, ZERO,  FALSE),
#  (TWO, ONE,   FALSE),
#  (TWO, ZERO,  FALSE),
#  (FIVE, FIVE, TRUE)
#])
#def test_eq(left, right, expected):
#  assert EQ(left)(right) is expected

#@pytest.mark.parametrize("left, right, expected",[
#  (ZERO, ZERO, ZERO),
#  (ONE,  ONE,  ONE),
#  (ONE,  TWO,  TWO),
#  (ONE, ZERO,  ONE),
#  (TWO, ONE,   TWO),
#  (TWO, ZERO,  TWO),
#  (FIVE, THREE, FIVE)
#])
#def test_max(left, right, expected):
#  assert MAX(left)(right) is expected

#@pytest.mark.parametrize("left, right, expected",[
#  (ZERO, ZERO, ZERO),
#  (ONE,  ONE,  ONE),
#  (ONE,  TWO,  ONE),
#  (ONE, ZERO,  ZERO),
#  (TWO, ONE,   ONE),
#  (TWO, ZERO,  ZERO),
#  (FIVE, THREE, THREE)
#])
#def test_min(left, right, expected):
#  assert MIN(left)(right) is expected
  
  
if __name__=="__main__":
  pytest(["-v"])
