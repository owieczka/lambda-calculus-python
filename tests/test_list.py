import pytest
from lambdacalculus.bool import TRUE, FALSE 
from lambdacalculus.natural import ZERO, ONE, TWO, THREE, FOUR, FIVE, NINE
from lambdacalculus.natural import ADD
from lambdacalculus.natural import LTE
from lambdacalculus.natural import decode_natural
from lambdacalculus.pair import CONS, CDR, CAR
from lambdacalculus.list import LIST, RANGE
from lambdacalculus.list import PREPEND, APPEND, INDEX
from lambdacalculus.list import REVERSE, REDUCE, MAP, FILTER, DROP, TAKE
from lambdacalculus.list import LENGTH
from lambdacalculus.list import ANY, ALL
from lambdacalculus.list import decode_list

@pytest.mark.parametrize("given",[
  [0],
  [0, 1],
  [0, 2, 4]
])
def test_prepend(given):
  list = LIST
  for el in reversed(given):
    list = PREPEND(list)(el)
  assert decode_list(list,100) == given

@pytest.mark.parametrize("given",[
  [0],
  [0, 1],
  [0, 2, 4]
])
def test_append(given):
  list = LIST
  for el in given:
    list = APPEND(list)(el)
  assert decode_list(list,100) == given

@pytest.mark.parametrize("given",[
  [0],
  [0, 1],
  [0, 2, 4]
])
def test_reverse(given):
  list = LIST
  for el in given:
    list = PREPEND(list)(el)
  assert decode_list(REVERSE(list),100) == given

@pytest.mark.parametrize("given, expected",[
  ([ZERO],0),
  ([ZERO, ONE],1),
  ([ZERO, ONE, TWO], 3),
  ([ZERO, ONE, TWO, THREE],6)
])
def test_reduce(given, expected):
  list = LIST
  for el in given:
    list = PREPEND(list)(el)
  assert decode_natural(REDUCE(ADD)(list)(ZERO)) == expected

@pytest.mark.parametrize("given, expected",[
  ([ZERO],[2]),
  ([ZERO, ONE],[2,3]),
  ([ZERO, ONE, TWO], [2,3,4]),
  ([ZERO, ONE, TWO, THREE],[2,3,4,5])
])
def test_map(given, expected):
  list = LIST
  for el in reversed(given):
    list = PREPEND(list)(el)
  list = MAP(ADD(TWO))(list)
  #print(expected)
  assert [decode_natural(n) for n in  decode_list(list,100)] == expected

@pytest.mark.parametrize("left, right, expected",[
  (ZERO, ZERO, []),
  (ZERO, THREE,[0,1,2]),
  (FOUR, NINE,[4,5,6,7,8]),
  (THREE, ONE, [])
])
def test_range(left, right, expected):
  list = RANGE(left)(right)
  assert [decode_natural(n) for n in  decode_list(list,100)] == expected

@pytest.mark.parametrize("given, expected",[
  ([ZERO],[]),
  ([ZERO, ONE],[]),
  ([ZERO, ONE, TWO], [2]),
  ([ZERO, ONE, TWO, THREE],[2,3])
])
def test_filter(given, expected):
  list = LIST
  for el in reversed(given):
    list = PREPEND(list)(el)
  list = FILTER(LTE(TWO))(list)
  #print(expected)
  assert [decode_natural(n) for n in  decode_list(list,100)] == expected

@pytest.mark.parametrize("given, number, expected",[
  ([ZERO],ONE,[]),
  ([ZERO, ONE, TWO],ONE,[1, 2]),
  ([ZERO, ONE, TWO], TWO, [2]),
  ([ZERO, ONE, TWO, THREE],THREE, [3])
])
def test_drop(given, number, expected):
  list = LIST
  for el in reversed(given):
    list = PREPEND(list)(el)
  list = DROP(number)(list)
  #print(expected)
  assert [decode_natural(n) for n in  decode_list(list,100)] == expected

@pytest.mark.parametrize("given, number, expected",[
  ([ZERO],ONE,[0]),
  ([ZERO, ONE, TWO],ONE,[0]),
  ([ZERO, ONE, TWO], TWO, [0, 1]),
  ([ZERO, ONE, TWO, THREE],THREE, [0, 1, 2])
])
def test_take(given, number, expected):
  list = LIST
  for el in reversed(given):
    list = PREPEND(list)(el)
  list = TAKE(number)(list)
  #print(expected)
  assert [decode_natural(n) for n in  decode_list(list,100)] == expected


@pytest.mark.parametrize("given, expected",[
  ([ZERO],1),
  ([ZERO, ONE, TWO],3),
  ([ZERO, ONE, TWO, THREE],4)
])
def test_length(given, expected):
  list = LIST
  for el in reversed(given):
    list = PREPEND(list)(el)
  assert decode_natural(LENGTH(list)) == expected

@pytest.mark.parametrize("given, number, expected",[
  ([ZERO], ZERO, 0),
  ([ZERO, ONE, TWO], ONE, 1),
  ([ZERO, ONE, TWO], TWO, 2),
  ([ZERO, ONE, TWO, THREE], THREE, 3)
])
def test_index(given, number, expected):
  list = LIST
  for el in reversed(given):
    list = PREPEND(list)(el)
  assert decode_natural(INDEX(number)(list)) == expected

@pytest.mark.parametrize("given,  expected",[
  ([], FALSE),
  ([FALSE, FALSE], FALSE),
  ([FALSE, TRUE], TRUE),
  ([FALSE, TRUE, FALSE], TRUE)
])
def test_any(given, expected):
  list = LIST
  for el in reversed(given):
    list = PREPEND(list)(el)
  assert ANY(list) is expected

@pytest.mark.parametrize("given,  expected",[
  ([], TRUE),
  ([FALSE], FALSE),
  ([TRUE], TRUE),
  ([TRUE, TRUE], TRUE),
  ([FALSE, FALSE], FALSE),
  ([FALSE, TRUE], FALSE),
  ([FALSE, TRUE, FALSE], FALSE)
])
def test_all(given, expected):
  list = LIST
  for el in reversed(given):
    list = PREPEND(list)(el)
  assert ALL(list) is expected


if __name__=="__main__":
  pytest(["-v"])
