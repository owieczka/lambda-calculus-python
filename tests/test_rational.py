import pytest
from lambdacalculus.natural import ZERO, ONE
from lambdacalculus.integer import INT_N2, INT_N1, INT_0, INT_1, INT_2
#from lambdacalculus.integer import INT_SUCC, INT_PRED, INT_ADD, INT_SUB, INT_MUL, INT_NEG, INT_POW
#from lambdacalculus.integer import INT_ISPOS, INT_ISZERO, INT_EQ, INT_GTE, INT_LTE, INT_GT, INT_LT
#from lambdacalculus.integer import INT_NORMALIZE
#from lambdacalculus.integer import INT_MAX, INT_MIN
#from lambdacalculus.integer import decode_integer
from lambdacalculus.rational import RAT_CREATE
from lambdacalculus.rational import RAT_ADD, RAT_MUL, RAT_SUB, RAT_NEG, RAT_INV, RAT_DIV
from lambdacalculus.rational import decode_rational
from lambdacalculus.bool import TRUE, FALSE

@pytest.mark.parametrize("given_n, given_m, expected",[
  (INT_0,ZERO,0/1),
  (INT_1,ZERO,1/1),
  (INT_2,ZERO,2/1),
  (INT_N1,ZERO,-1/1),
  (INT_N2,ZERO,-2/1),
  (INT_0,ZERO,0/1),
  (INT_1,ONE,1/2),
  (INT_2,ONE,2/2),
  (INT_N1,ONE,-1/2),
  (INT_N2,ONE,-2/2),
])
def test_decode_rational(given_n,given_m, expected):
  assert decode_rational(RAT_CREATE(given_n)(given_m)) == expected

#@pytest.mark.parametrize("given, expected",[
#  (INT_1,  TRUE),
#  (INT_2,  TRUE),
#  (INT_N1, FALSE),
#  (INT_N2, FALSE),
#  (INT_0, TRUE),
#])
#def test_ispos(given, expected):
#  assert INT_ISPOS(given) is expected

@pytest.mark.parametrize("left_n, left_m, right_n, right_m, expected",[
  (INT_0, ZERO, INT_0, ZERO, 0),
  (INT_0, ZERO, INT_1, ZERO, 1),
  (INT_1, ZERO, INT_2, ZERO, 3),
  (INT_N1, ZERO, INT_1, ZERO, 0),
  (INT_1, ZERO, INT_N1, ZERO, 0),
  (INT_2, ZERO, INT_N1, ZERO, 1),
  (INT_N2, ZERO, INT_1, ZERO, -1),
  (INT_N2, ZERO, INT_N1, ZERO, -3),
  (INT_0, ONE, INT_0, ZERO, 0/2+0),
  (INT_0, ONE, INT_1, ZERO, 0/2+1),
  (INT_1, ONE, INT_2, ZERO, 1/2+2),
  (INT_N1, ONE, INT_1, ZERO, -1/2+1),
  (INT_1, ONE, INT_N1, ZERO, 1/2-1),
  (INT_2, ONE, INT_N1, ZERO, 2/2-1),
  (INT_N2, ONE, INT_1, ZERO, -2/2+1),
  (INT_N2, ONE, INT_N1, ZERO, -2/2-1),
  (INT_0, ONE, INT_0, ONE, 0/2+0/2),
  (INT_0, ONE, INT_1, ONE, 0/2+1/2),
  (INT_1, ONE, INT_2, ONE, 1/2+2/2),
  (INT_N1, ONE, INT_1, ONE, -1/2+1/2),
  (INT_1, ONE, INT_N1, ONE, 1/2-1/2),
  (INT_2, ONE, INT_N1, ONE, 2/2-1/2),
  (INT_N2, ONE, INT_1, ONE, -2/2+1/2),
  (INT_N2, ONE, INT_N1, ONE, -2/2-1/2),
  (INT_0, ZERO, INT_0, ONE, 0/1+0/2),
  (INT_0, ZERO, INT_1, ONE, 0/1+1/2),
  (INT_1, ZERO, INT_2, ONE, 1/1+2/2),
  (INT_N1, ZERO, INT_1, ONE, -1/1+1/2),
  (INT_1, ZERO, INT_N1, ONE, 1/1-1/2),
  (INT_2, ZERO, INT_N1, ONE, 2/1-1/2),
  (INT_N2, ZERO, INT_1, ONE, -2/1+1/2),
  (INT_N2, ZERO, INT_N1, ONE, -2/1-1/2),
])
def test_add(left_n, left_m, right_n, right_m, expected):
  assert decode_rational(RAT_ADD(RAT_CREATE(left_n)(left_m))(RAT_CREATE(right_n)(right_m))) == expected

@pytest.mark.parametrize("left_n, left_m, right_n, right_m, expected",[
  (INT_0, ZERO, INT_0, ZERO, 0/1*0/1),
  (INT_0, ZERO, INT_1, ZERO, 0/1*1/1),
  (INT_1, ZERO, INT_2, ZERO, 1/1*2/1),
  (INT_N1, ZERO, INT_1, ZERO, -1/1*1/1),
  (INT_1, ZERO, INT_N1, ZERO, 1/1*-1/1),
  (INT_2, ZERO, INT_N1, ZERO, 2/1*-1/1),
  (INT_N2, ZERO, INT_1, ZERO, -2/1*1/1),
  (INT_N2, ZERO, INT_N1, ZERO, -2/1*-1/1),
  (INT_0, ONE, INT_0, ZERO, 0/2*0),
  (INT_0, ONE, INT_1, ZERO, 0/2*1),
  (INT_1, ONE, INT_2, ZERO, 1/2*2),
  (INT_N1, ONE, INT_1, ZERO, -1/2*1),
  (INT_1, ONE, INT_N1, ZERO, 1/2*-1),
  (INT_2, ONE, INT_N1, ZERO, 2/2*-1),
  (INT_N2, ONE, INT_1, ZERO, -2/2*1),
  (INT_N2, ONE, INT_N1, ZERO, -2/2*-1),
  (INT_0, ONE, INT_0, ONE, 0/2*0/2),
  (INT_0, ONE, INT_1, ONE, 0/2*1/2),
  (INT_1, ONE, INT_2, ONE, 1/2*2/2),
  (INT_N1, ONE, INT_1, ONE, -1/2*1/2),
  (INT_1, ONE, INT_N1, ONE, 1/2*-1/2),
  (INT_2, ONE, INT_N1, ONE, 2/2*-1/2),
  (INT_N2, ONE, INT_1, ONE, -2/2*1/2),
  (INT_N2, ONE, INT_N1, ONE, -2/2*-1/2),
  (INT_0, ZERO, INT_0, ONE, 0/1*0/2),
  (INT_0, ZERO, INT_1, ONE, 0/1*1/2),
  (INT_1, ZERO, INT_2, ONE, 1/1*2/2),
  (INT_N1, ZERO, INT_1, ONE, -1/1*1/2),
  (INT_1, ZERO, INT_N1, ONE, 1/1*-1/2),
  (INT_2, ZERO, INT_N1, ONE, 2/1*-1/2),
  (INT_N2, ZERO, INT_1, ONE, -2/1*1/2),
  (INT_N2, ZERO, INT_N1, ONE, -2/1*-1/2),
])
def test_mul(left_n, left_m, right_n, right_m, expected):
  assert decode_rational(RAT_MUL(RAT_CREATE(left_n)(left_m))(RAT_CREATE(right_n)(right_m))) == expected

@pytest.mark.parametrize("given_n, given_m, expected",[
  (INT_1, ZERO, -1/1),
  (INT_2, ZERO, -2/1),
  (INT_N1,ZERO, 1/1),
  (INT_N2,ZERO, 2/1),
  (INT_0, ZERO, 0/1),
  (INT_1, ONE, -1/2),
  (INT_2, ONE, -2/2),
  (INT_N1,ONE, 1/2),
  (INT_N2,ONE, 2/2),
  (INT_0, ONE, 0/2),
])
def test_neg(given_n, given_m, expected):
  assert decode_rational(RAT_NEG(RAT_CREATE(given_n)(given_m))) == expected

@pytest.mark.parametrize("given_n, given_m, expected",[
  (INT_1, ZERO, 1/1),
  (INT_2, ZERO, 1/2),
  (INT_N1,ZERO, -1/1),
  (INT_N2,ZERO, -1/2),
  #(INT_0, ZERO, 1/0),
  (INT_1, ONE, 2/1),
  (INT_2, ONE, 2/2),
  (INT_N1,ONE, -2/1),
  (INT_N2,ONE, -2/2),
  #(INT_0, ONE, 2/0),
])
def test_inv(given_n, given_m, expected):
  assert decode_rational(RAT_INV(RAT_CREATE(given_n)(given_m))) == expected

#@pytest.mark.parametrize("left, right, expected",[
#  (INT_0, INT_0, 0),
#  (INT_0, INT_1, 1),
#  (INT_1, INT_2, 3),
#  (INT_N1, INT_1, 0),
#  (INT_1, INT_N1, 0),
#  (INT_2, INT_N1, 1),
#  (INT_N2, INT_1, -1),
#  (INT_N2, INT_N1, -3)
#])
#def test_normalize(left, right, expected):
#  assert decode_integer(INT_NORMALIZE(INT_ADD(left)(right))) == expected


#@pytest.mark.parametrize("left, right, expected",[
#  (INT_0, INT_1,   0),
#  (INT_0, INT_2,   0),
#  (INT_1, INT_2,   1),
#  (INT_2, INT_2,   4),
#  (INT_SUCC(INT_2),INT_2,   9),
#  (INT_SUCC(INT_2),INT_SUCC(INT_2), 27),
#  (INT_N1, INT_2,   1),
#  (INT_N2, INT_2,   4),
#  (INT_PRED(INT_N2),INT_2,   9),
#  (INT_PRED(INT_N2),INT_SUCC(INT_2), -27)
#])
#def test_pow(left, right, expected):
#  assert decode_integer(INT_POW(left)(right)) == expected

#@pytest.mark.parametrize("given, expected",[
#  (INT_0, -1),
#  (INT_1,  0),
#  (INT_2,  1),
#  (INT_N1,-2)
#])
#def test_pred(given, expected):
#  assert decode_integer(INT_PRED(given)) == expected

@pytest.mark.parametrize("left_n, left_m, right_n, right_m, expected",[
  (INT_0, ZERO, INT_0, ZERO, 0),
  (INT_0, ZERO, INT_1, ZERO, -1),
  (INT_1, ZERO, INT_2, ZERO, 1-2),
  (INT_N1, ZERO, INT_1, ZERO, -1-1),
  (INT_1, ZERO, INT_N1, ZERO, 1+1),
  (INT_2, ZERO, INT_N1, ZERO, 2+1),
  (INT_N2, ZERO, INT_1, ZERO, -2-1),
  (INT_N2, ZERO, INT_N1, ZERO, -2+1),
  (INT_0, ONE, INT_0, ZERO, 0/2-0),
  (INT_0, ONE, INT_1, ZERO, 0/2-1),
  (INT_1, ONE, INT_2, ZERO, 1/2-2),
  (INT_N1, ONE, INT_1, ZERO, -1/2-1),
  (INT_1, ONE, INT_N1, ZERO, 1/2+1),
  (INT_2, ONE, INT_N1, ZERO, 2/2+1),
  (INT_N2, ONE, INT_1, ZERO, -2/2-1),
  (INT_N2, ONE, INT_N1, ZERO, -2/2+1),
  (INT_0, ONE, INT_0, ONE, 0/2-0/2),
  (INT_0, ONE, INT_1, ONE, 0/2-1/2),
  (INT_1, ONE, INT_2, ONE, 1/2-2/2),
  (INT_N1, ONE, INT_1, ONE, -1/2-1/2),
  (INT_1, ONE, INT_N1, ONE, 1/2+1/2),
  (INT_2, ONE, INT_N1, ONE, 2/2+1/2),
  (INT_N2, ONE, INT_1, ONE, -2/2-1/2),
  (INT_N2, ONE, INT_N1, ONE, -2/2+1/2),
  (INT_0, ZERO, INT_0, ONE, 0/1-0/2),
  (INT_0, ZERO, INT_1, ONE, 0/1-1/2),
  (INT_1, ZERO, INT_2, ONE, 1/1-2/2),
  (INT_N1, ZERO, INT_1, ONE, -1/1-1/2),
  (INT_1, ZERO, INT_N1, ONE, 1/1+1/2),
  (INT_2, ZERO, INT_N1, ONE, 2/1+1/2),
  (INT_N2, ZERO, INT_1, ONE, -2/1-1/2),
  (INT_N2, ZERO, INT_N1, ONE, -2/1+1/2),
])
def test_sub(left_n, left_m, right_n, right_m, expected):
  assert decode_rational(RAT_SUB(RAT_CREATE(left_n)(left_m))(RAT_CREATE(right_n)(right_m))) == expected

@pytest.mark.parametrize("left_n, left_m, right_n, right_m, expected",[
  #(INT_0, ZERO, INT_0, ZERO, 0/1/(0/1)),
  (INT_0, ZERO, INT_1, ZERO, 0/1/(1/1)),
  (INT_1, ZERO, INT_2, ZERO, 1/1/(2/1)),
  (INT_N1, ZERO, INT_1, ZERO, -1/1/(1/1)),
  (INT_1, ZERO, INT_N1, ZERO, 1/1/(-1/1)),
  (INT_2, ZERO, INT_N1, ZERO, 2/1/(-1/1)),
  (INT_N2, ZERO, INT_1, ZERO, -2/1/(1/1)),
  (INT_N2, ZERO, INT_N1, ZERO, -2/1/(-1/1)),
  #(INT_0, ONE, INT_0, ZERO, 0/2/0),
  (INT_0, ONE, INT_1, ZERO, 0/2/1),
  (INT_1, ONE, INT_2, ZERO, 1/2/2),
  (INT_N1, ONE, INT_1, ZERO, -1/2/1),
  (INT_1, ONE, INT_N1, ZERO, 1/2/(-1)),
  (INT_2, ONE, INT_N1, ZERO, 2/2/(-1)),
  (INT_N2, ONE, INT_1, ZERO, -2/2/1),
  (INT_N2, ONE, INT_N1, ZERO, -2/2/(-1)),
  #(INT_0, ONE, INT_0, ONE, 0/2/(0/2)),
  (INT_0, ONE, INT_1, ONE, 0/2/(1/2)),
  (INT_1, ONE, INT_2, ONE, 1/2/(2/2)),
  (INT_N1, ONE, INT_1, ONE, -1/2/(1/2)),
  (INT_1, ONE, INT_N1, ONE, 1/2/(-1/2)),
  (INT_2, ONE, INT_N1, ONE, 2/2/(-1/2)),
  (INT_N2, ONE, INT_1, ONE, -2/2/(1/2)),
  (INT_N2, ONE, INT_N1, ONE, -2/2/(-1/2)),
  #(INT_0, ZERO, INT_0, ONE, 0/1/(0/2)),
  (INT_0, ZERO, INT_1, ONE, 0/1/(1/2)),
  (INT_1, ZERO, INT_2, ONE, 1/1/(2/2)),
  (INT_N1, ZERO, INT_1, ONE, -1/1/(1/2)),
  (INT_1, ZERO, INT_N1, ONE, 1/1/(-1/2)),
  (INT_2, ZERO, INT_N1, ONE, 2/1/(-1/2)),
  (INT_N2, ZERO, INT_1, ONE, -2/1/(1/2)),
  (INT_N2, ZERO, INT_N1, ONE, -2/1/(-1/2)),
])
def test_div(left_n, left_m, right_n, right_m, expected):
  assert decode_rational(RAT_DIV(RAT_CREATE(left_n)(left_m))(RAT_CREATE(right_n)(right_m))) == expected
  
#@pytest.mark.parametrize("left, right, expected",[
#  (ZERO, ZERO, 0),
#  (ZERO, ONE,  1),
#  (ONE,  TWO,  1),
#  (ONE, ZERO,  1),
#  (TWO, ONE,   1),
#  (TWO, ZERO,  2)
#])
#def test_diff(left, right, expected):
#  assert decode_natural(DIFF(left)(right)) == expected

#@pytest.mark.parametrize("given, expected",[
#  (INT_0, TRUE),
#  (INT_1, FALSE),
#  (INT_2, FALSE),
#  (INT_N1,FALSE),
#  (INT_PRED(INT_SUCC(INT_0)), TRUE)
#])
#def test_iszero(given, expected):
#  assert INT_ISZERO(given) is expected

#@pytest.mark.parametrize("left, right, expected",[
#  (INT_0, INT_0, TRUE),
#  (INT_0, INT_1,  FALSE),
#  (INT_1, INT_2,  FALSE),
#  (INT_1, INT_0,  TRUE),
#  (INT_2, INT_1,  TRUE),
#  (INT_2, INT_0,  TRUE),
#  (INT_SUCC(INT_ADD(INT_2)(INT_2)), INT_2, TRUE),
#  (INT_0, INT_N1,  TRUE),
#  (INT_1, INT_N2,  TRUE),
#  (INT_2, INT_N1,  TRUE),
#  (INT_N2, INT_0,  FALSE),
#  (INT_N1, INT_0,  FALSE),
#  (INT_N1, INT_N2,  TRUE),
#  (INT_N2, INT_N1,  FALSE),
#  (INT_N1, INT_2,  FALSE),
#  (INT_N2, INT_1,  FALSE),
#])
#def test_gte(left, right, expected):
#  assert INT_GTE(left)(right) is expected
#  assert INT_LT(left)(right) is not expected

#@pytest.mark.parametrize("left, right, expected",[
#  (INT_0, INT_0, TRUE),
#  (INT_0, INT_1,  TRUE),
#  (INT_1, INT_2,  TRUE),
#  (INT_1, INT_0,  FALSE),
#  (INT_2, INT_1,  FALSE),
#  (INT_2, INT_0,  FALSE),
#  (INT_SUCC(INT_ADD(INT_2)(INT_2)), INT_2, FALSE),
#  (INT_0, INT_N1,  FALSE),
#  (INT_1, INT_N2,  FALSE),
#  (INT_2, INT_N1,  FALSE),
#  (INT_N2, INT_0,  TRUE),
#  (INT_N1, INT_0,  TRUE),
#  (INT_N1, INT_N2,  FALSE),
#  (INT_N2, INT_N1,  TRUE),
#  (INT_N1, INT_2,  TRUE),
#  (INT_N2, INT_1,  TRUE),
#])
#def test_lte(left, right, expected):
#  assert INT_LTE(left)(right) is expected
#  assert INT_GT(left)(right) is not expected

#@pytest.mark.parametrize("left, right, expected",[
#  (INT_0, INT_0, TRUE),
#  (INT_1, INT_1, TRUE),
#  (INT_N1, INT_N1, TRUE),
#  (INT_1, INT_2,  FALSE),
#  (INT_1, INT_0,  FALSE),
#  (INT_2, INT_1,   FALSE),
#  (INT_2, INT_0,  FALSE),
#  (INT_N1, INT_N1, TRUE),
#  (INT_1, INT_N2,  FALSE),
#  (INT_N1, INT_2,  FALSE),
#  (INT_N1, INT_N2,  FALSE),
#  (INT_N1, INT_0,  FALSE),
#  (INT_2, INT_N1,   FALSE),
#  (INT_N2, INT_N1,   FALSE),
#  (INT_N2, INT_1,   FALSE),
#  (INT_N2, INT_0,  FALSE),
#])
#def test_eq(left, right, expected):
#  assert INT_EQ(left)(right) is expected

#@pytest.mark.parametrize("left, right, expected",[
#  (INT_0, INT_0, INT_0),
#  (INT_0, INT_1, INT_1),
#  (INT_1, INT_2, INT_2),
#  (INT_1, INT_0, INT_1),
#  (INT_2, INT_1, INT_2),
#  (INT_2, INT_0, INT_2),
#  (INT_0, INT_N1, INT_0),
#  (INT_1, INT_N2, INT_1),
#  (INT_2, INT_N1, INT_2),
#  (INT_N1, INT_2, INT_2),
#  (INT_N1, INT_0, INT_0),
#  (INT_N2, INT_1, INT_1),
#  (INT_N2, INT_0, INT_0),
#  (INT_N1, INT_N2, INT_N1),
#  (INT_N2, INT_N1, INT_N1),
#])
#def test_max(left, right, expected):
#  assert INT_MAX(left)(right) is expected

#@pytest.mark.parametrize("left, right, expected",[
#  (INT_0, INT_0, INT_0),
#  (INT_0, INT_1, INT_0),
#  (INT_1, INT_2, INT_1),
#  (INT_1, INT_0, INT_0),
#  (INT_2, INT_1, INT_1),
#  (INT_2, INT_0, INT_0),
#  (INT_0, INT_N1, INT_N1),
#  (INT_1, INT_N2, INT_N2),
#  (INT_2, INT_N1, INT_N1),
#  (INT_N1, INT_2, INT_N1),
#  (INT_N1, INT_0, INT_N1),
#  (INT_N2, INT_1, INT_N2),
#  (INT_N2, INT_0, INT_N2),
#  (INT_N1, INT_N2, INT_N2),
#  (INT_N2, INT_N1, INT_N2),
#])
#def test_min(left, right, expected):
#  assert INT_MIN(left)(right) is expected
  
if __name__=="__main__":
  pytest(["-v"])
