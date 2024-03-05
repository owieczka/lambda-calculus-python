#from .bool import TRUE, FALSE, IDENTYTY, AND
from .natural import ZERO #, ONE, TWO
from .natural import SUCC, ADD, MUL, PRED
#from .natural import GTE, LTE, GT, LT, EQ
from .natural import decode_natural
#from .aritmetic import EVEN, ODD
from .integer import INT_CREATE
from .integer import INT_ADD, INT_MUL, INT_SUB, INT_NEG, INT_ABS_NAT
from .integer import INT_ISPOS, INT_ISZERO
from .integer import decode_integer
from .pair import CONS, CAR, CDR

##########################
# Radionals
##########################

# PAIR(i)(n) <=> (i/(n+1)) 
# integer i 
# natural n
RAT_CREATE = CONS

##########################
# Arithmetic
##########################

RAT_ADD = lambda a: lambda b: CONS(
    INT_ADD
    (
      INT_MUL(CAR(a))(INT_CREATE(SUCC(CDR(b)))(ZERO)) #a_i*(b_n+1)
    )
    (
      INT_MUL(CAR(b))(INT_CREATE(SUCC(CDR(a)))(ZERO)) #b_i*(a_n+1)
    )
  )(
    ADD
    (
      MUL(CDR(a))(CDR(b)) # a_n * b_n
    )
    (
      ADD(CDR(a))(CDR(b)) # a_n + b_n
    )
  )
# a + b = a_i/(a_n+1) + b_i/(b_n+1) = (a_i*(b_n+1) + b_i*(a_n+1))/((a_n*b_n + a_n + b_n) + 1)

RAT_MUL = lambda a: lambda b: CONS(
    INT_MUL(CAR(a))(CAR(b)) # a_i*b_i
  )(
    ADD
    (
      MUL(CDR(a))(CDR(b)) # a_n * b_n
    )
    (
      ADD(CDR(a))(CDR(b)) # a_n + b_n
    )
  )
# a * b = a_i/(a_n+1) * b_i/(b_n+1) = (a_i*b_i)/((a_n*b_n + a_n+b_n)+1)

RAT_ISPOS = lambda n: INT_ISPOS(CAR(n)) 

RAT_SUB = lambda a: lambda b: CONS(
    INT_SUB
    (
      INT_MUL(CAR(a))(INT_CREATE(SUCC(CDR(b)))(ZERO)) #a_i*(b_n+1)
    )
    (
      INT_MUL(CAR(b))(INT_CREATE(SUCC(CDR(a)))(ZERO)) #b_i*(a_n+1)
    )
  )(
    ADD
    (
      MUL(CDR(a))(CDR(b)) # a_n * b_n
    )
    (
      ADD(CDR(a))(CDR(b)) # a_n + b_n
    )
  )
# a - b = a_i/(a_n+1) - b_i/(b_n+1) = (a_i*(b_n+1) - b_i*(a_n+1))/((a_n*b_n + a_n + b_n) + 1)

RAT_NEG = lambda n: CONS(INT_NEG(CAR(n)))(CDR(n))         #-n = -n_n/(n_m+1)

RAT_INV = lambda n: INT_ISPOS(CAR(n))(  # n>=0
    CONS(
      INT_CREATE(SUCC(CDR(n)))(ZERO)
    )(
      PRED(INT_ABS_NAT(CAR(n)))
    )
  )(
    CONS(
      INT_CREATE(ZERO)(SUCC(CDR(n)))
    )(
      PRED(INT_ABS_NAT(CAR(n)))
    )
  )
# [n_n / (n_m+1)]^(-1) = (n_m + 1) / ((n_n-1)+1

RAT_DIV = lambda a: lambda b: RAT_MUL(a)(RAT_INV(b))

# ONLY  a^b if b>0
#INT_POW = lambda a: lambda b: (
#    lambda na: lambda nb:
#    CONS
#    (
#      ADD
#      ( POW(CAR(na))(CAR(nb)) )
#      (
#        EVEN(CAR(nb))
#        ( POW(CDR(na))(CAR(nb)) )
#        ( ZERO )
#      )
#    )
#    (
#      ODD(CAR(nb))
#      ( POW(CDR(na))(CAR(nb)) )
#      ( ZERO )
#    )
#  )(INT_NORMALIZE(a))(INT_NORMALIZE(b))
 
##########################
# Numbers
##########################

##########################
# Checks
##########################

RAT_ISZERO = lambda n: INT_ISZERO(CAR(n)) #n==0
 
#INT_GTE = lambda a: lambda b: GTE(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a>=b <=> (a_n-a_m)>=(b_n-b_m) <=> (a_n+b_m)>=(a_m+b_n)
#INT_LTE = lambda a: lambda b: LTE(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a<=b <=> (a_n-a_m)<=(b_n-b_m) <=> (a_n+b_m)<=(a_m+b_n)
#INT_GT = lambda a: lambda b: GT(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a>b <=> (a_n-a_m)>(b_n-b_m) <=> (a_n+b_m)>(a_m+b_n)
#INT_LT = lambda a: lambda b: LT(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a<b <=> (a_n-a_m)<(b_n-b_m) <=> (a_n+b_m)<(a_m+b_n)
#INT_EQ = lambda a: lambda b: EQ(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a==b <=> (a_n-a_m)==(b_n-b_m) <=> (a_n+b_m)==(a_m+b_n) 

##########################
# Other
##########################

#INT_MIN = lambda a: lambda b: INT_LTE(a)(b)(a)(b)
#INT_MAX = lambda a: lambda b: INT_GTE(a)(b)(a)(b)

##########################
# Decode Numbers
##########################

def decode_rational(num):
  return decode_integer(CAR(num))/(decode_natural(CDR(num))+1)
