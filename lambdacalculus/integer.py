from .bool import TRUE, FALSE, IDENTYTY, AND
from .natural import ZERO, ONE, TWO
from .natural import SUCC, ADD, MUL, SUB, POW
from .natural import MAX
from .natural import GTE, LTE, GT, LT, EQ
from .natural import decode_natural
from .aritmetic import EVEN, ODD
from .pair import CONS, CAR, CDR

##########################
# Integer
##########################

# PAIR(n)(m) <=> (n-m) 
# positive n >= m
# negative n < m
INT_CREATE = CONS

##########################
# Arithmetic
##########################

INT_SUCC = lambda n: CONS(SUCC(CAR(n)))(CDR(n))       # n + 1 = (n_n -  n_m) + 1 = ((n_n + 1) - n_m)
INT_ADD = lambda a: lambda b: CONS(ADD(CAR(a))(CAR(b)))(ADD(CDR(a))(CDR(b))) # a + b = (a_n - a_m) + (b_n - b_m) = ((a_n + b_n) - (a_m + b_m))
INT_MUL = lambda a: lambda b: CONS(ADD(MUL(CAR(a))(CAR(b)))(MUL(CDR(a))(CDR(b))))(ADD(MUL(CDR(a))(CAR(b)))(MUL(CAR(a))(CDR(b))))    # a * b = (a_n - a_m) * (b_n - b_m) = ((a_n*b_n + a_m*b_m) - (a_m*b_n + a_n*b_m))
#POW = lambda a: lambda b: b(a)                  # a ^ b = (a_n-a_m)^b_n / (a_n-a_m)^b_m

INT_PRED = lambda n: CONS(CAR(n))(SUCC(CDR(n)))  # n - 1 = (n_n - n_m) - 1 = (n_n - (n_m + 1))
INT_ISPOS = lambda n: GTE(CAR(n))(CDR(n))        # CAR >= CDR 
INT_SUB = lambda a: lambda b: CONS(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a - b = (a_n - a_m) - (b_n - b_m) = ((a_n + b_m) - (a_m + b_n))
INT_NEG = lambda n: CONS(CDR(n))(CAR(n))         #-n = -(n_n - n_m) = (n_m - n_n)
#DIFF = lambda a: lambda b: ADD(SUB(a)(b))(SUB(b)(a))

INT_NORMALIZE = lambda n: CONS(SUB(CAR(n))(CDR(n)))(SUB(CDR(n))(CAR(n))) # n = (n_n - n_m) = ((n_n-n_m) - 0) = (0 - (n_m-n_n))

INT_ABS_NAT = lambda n: MAX(SUB(CAR(n))(CDR(n)))(SUB(CDR(n))(CAR(n))) # |n| in natural numbers
INT_ABS = lambda n: CONS(INT_ABS_NAT(n))(ZERO) # |n| in integer numbers

# ONLY  a^b if b>0
INT_POW = lambda a: lambda b: (
    lambda na: lambda nb:
    CONS
    (
      ADD
      ( POW(CAR(na))(CAR(nb)) )
      (
        EVEN(CAR(nb))
        ( POW(CDR(na))(CAR(nb)) )
        ( ZERO )
      )
    )
    (
      ODD(CAR(nb))
      ( POW(CDR(na))(CAR(nb)) )
      ( ZERO )
    )
  )(INT_NORMALIZE(a))(INT_NORMALIZE(b))
 
##########################
# Numbers
##########################
INT_N2 = INT_CREATE(ZERO)(TWO)
INT_N1 = INT_CREATE(ZERO)(ONE)
INT_0 = INT_CREATE(ZERO)(ZERO)
INT_1 = INT_CREATE(ONE)(ZERO)
INT_2 = INT_CREATE(TWO)(ZERO)

##########################
# Checks
##########################

INT_ISZERO = lambda n: EQ(CAR(n))(CDR(n)) #n==0 <=> n_n==n_m 
INT_GTE = lambda a: lambda b: GTE(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a>=b <=> (a_n-a_m)>=(b_n-b_m) <=> (a_n+b_m)>=(a_m+b_n)
INT_LTE = lambda a: lambda b: LTE(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a<=b <=> (a_n-a_m)<=(b_n-b_m) <=> (a_n+b_m)<=(a_m+b_n)
INT_GT = lambda a: lambda b: GT(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a>b <=> (a_n-a_m)>(b_n-b_m) <=> (a_n+b_m)>(a_m+b_n)
INT_LT = lambda a: lambda b: LT(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a<b <=> (a_n-a_m)<(b_n-b_m) <=> (a_n+b_m)<(a_m+b_n)
INT_EQ = lambda a: lambda b: EQ(ADD(CAR(a))(CDR(b)))(ADD(CDR(a))(CAR(b))) # a==b <=> (a_n-a_m)==(b_n-b_m) <=> (a_n+b_m)==(a_m+b_n) 

##########################
# Other
##########################

INT_MIN = lambda a: lambda b: INT_LTE(a)(b)(a)(b)
INT_MAX = lambda a: lambda b: INT_GTE(a)(b)(a)(b)

##########################
# Decode Numbers
##########################

def decode_integer(num):
  return decode_natural(CAR(num))-decode_natural(CDR(num))
