from lambdacalculus.natural import ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN
from lambdacalculus.natural import MUL, SUCC, ADD
from lambdacalculus.natural import EQ, GTE
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
NAT_100 = MUL(MUL(TEN)(TEN))(TWO)
list2 = RANGE(NAT_0)(NAT_100)
list3 = MAP(lambda x: TRUE)(list2)

#NAT_100 72s 23s (native)
#NAT_200 xxx 529s (native)

# Mark FALSE all mulplicitative of n starting from a
# idx: index of element processed
# a: current multiplicative
# n: number to markout 
MARKOUT_MULTIPLICATIVE_OF_N_INNER = Y(
  lambda f: lambda idx: lambda a: lambda n: lambda list: EMPTY(list)
  (lambda _: LIST)
  (lambda _: 
  PREPEND( f(SUCC(idx))(EQ(idx)(a)(ADD(a)(n))(a))(n)(TAIL(list))
  )(
    EQ(idx)(a)(FALSE)(HEAD(list))
  )
  )
  (TRUE)
)
MARKOUT_MULTIPLICATIVE_OF_N = lambda n: lambda list: MARKOUT_MULTIPLICATIVE_OF_N_INNER(ZERO)(MUL(TWO)(n))(n)(list)


#list4=MARKOUT_MULTIPLICATIVE_OF_N(TWO)(list3)
#list4=MARKOUT_MULTIPLICATIVE_OF_N(THREE)(list4)
#list4=MARKOUT_MULTIPLICATIVE_OF_N(FOUR)(list4)

# Find all primes in range idx n 
SIERVE = Y(
  lambda f: lambda idx: lambda n: lambda list: GTE(idx)(n)
  (lambda _: list)
  (lambda _: f(SUCC(idx))(n)(MARKOUT_MULTIPLICATIVE_OF_N(idx)(list)))
  (TRUE)
)

list4 = SIERVE(NAT_2)(NAT_100)(list3)
#list5 = FILTER(lambda x: INDEX(x)(list4))(list2)

bbb = Y(
  lambda f: lambda p: lambda list: lambda ret: OR(EMPTY(p))(EMPTY(list))
  (lambda _: ret)
  (lambda _: f(TAIL(p))(TAIL(list))(
    HEAD(p)(PREPEND(ret)(HEAD(list)))(ret)
    )
  )
  (TRUE)
)

list5 = bbb(list4)(list2)(LIST)
list5 = REVERSE(list5)

aaa = Y(
  lambda f: lambda p: lambda list: OR(EMPTY(p))(EMPTY(list))
  (lambda _: LIST)
  (lambda _:
    HEAD(p)
    (
      PREPEND(f(TAIL(p))(TAIL(list)))(HEAD(list))
    )
    (
      f(TAIL(p))(TAIL(list))
    )
  )
  (TRUE)
)

#list5 = aaa(list4)(list2)
time_end = time.time()

print(f"Time: {time_end-time_start}")

print(decode_natural(NAT_20))
print([decode_natural(nat) for nat in decode_list(list2,300)])
print([nat("True")("False") for nat in decode_list(list4,300)])
print([decode_natural(nat) for nat in decode_list(list5,300)])
##########################

