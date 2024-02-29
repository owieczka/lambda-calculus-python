from lambdacalculus.natural import ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN
from lambdacalculus.natural import MUL, SUCC, ADD
from lambdacalculus.natural import EQ, GTE, GT, LT, LTE
from lambdacalculus.natural import decode_natural
from lambdacalculus.list import RANGE, MAP, EMPTY, LIST, APPEND, PREPEND, HEAD, TAIL, FILTER, INDEX, REVERSE
from lambdacalculus.list import decode_list
from lambdacalculus.bool import FALSE, TRUE, OR
from lambdacalculus.combinators import Y

import time

time_start = time.time()

NAT_0 = ZERO
NAT_2 = TWO
NAT_20 = MUL(TEN)(TWO)
NAT_100 = MUL(TEN)(TEN)
NAT_200 = MUL(NAT_100)(NAT_2)
#NAT_100 16s 5.44s 4.18s
#NAT_200 xxx 115s 68s
list2 = RANGE(NAT_0)(NAT_200)


REMOVE_MULTIPLICATIVE_OF_N_INTERNAL = Y(
  lambda f: lambda a: lambda n: lambda list: lambda oldlist: EMPTY(oldlist)
  (lambda _: list)
  (lambda _: 
    f
    (
      LTE(a)(HEAD(oldlist)) # a<= HEAD
      (ADD(a)(n))
      (a)
    )
    (n)
    (
      LTE(a)(HEAD(oldlist)) # a<= HEAD
      (list)
      (PREPEND(list)(HEAD(oldlist)))
    )
    (
      LT(a)(HEAD(oldlist)) #a < HEAD
      (oldlist)
      (
        TAIL(oldlist)
      )
    )
  )
  (TRUE)
)


REMOVE_MULTIPLICATIVE_OF_N_INTERNAL2 = Y(
  lambda f: lambda a: lambda n: lambda list: lambda oldlist: EMPTY(oldlist)
  (lambda _: list)
  (lambda _: (lambda lte:
    f
    (
      lte # a<= HEAD
      (ADD(a)(n))
      (a)
    )
    (n)
    (
      lte # a<= HEAD
      (list)
      (PREPEND(list)(HEAD(oldlist)))
    )
    (
      LT(a)(HEAD(oldlist)) #a < HEAD
      (oldlist)
      (
        TAIL(oldlist)
      )
    )
    )(LTE(a)(HEAD(oldlist)))
  )
  (TRUE)
)

#list5 = REMOVE_MULTIPLICATIVE_OF_N_INTERNAL(MUL(TWO)(TWO))(TWO)(LIST)(list2)
#list5 = REVERSE(list5)
#list5 = REMOVE_MULTIPLICATIVE_OF_N_INTERNAL(MUL(TWO)(THREE))(THREE)(LIST)(list5)
#list5 = REVERSE(list5)

SIERVE = Y(
  lambda f: lambda idx: lambda n: lambda list: GTE(idx)(n)
  (lambda _: list)
  (lambda _: f(SUCC(idx))(n)(
    #MARKOUT_MULTIPLICATIVE_OF_N(idx)(list))
    REVERSE(REMOVE_MULTIPLICATIVE_OF_N_INTERNAL2(MUL(TWO)(idx))(idx)(LIST)(list)))
  )
  (TRUE)
)

list5 = SIERVE(NAT_2)(NAT_200)(list2)


time_end = time.time()

print(f"Time: {time_end-time_start}")

print(decode_natural(NAT_20))
print([decode_natural(nat) for nat in decode_list(list2,300)])
#print([nat("True")("False") for nat in decode_list(list4,200)])
print([decode_natural(nat) for nat in decode_list(list5,300)])
##########################

