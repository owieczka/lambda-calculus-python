from .bool import NOT, TRUE, FALSE, XOR, XNOR
from .natural import ADD, LTE, DIFF, MUL
from .pair import CONS, CAR, CDR

##########################
# Signed
##########################

# Create signed number 
# s - sign 
# n - value
SIGNED = CONS

# Return a sign of a number
ISPOS = CAR
ISNEG = lambda p: NOT(ISPOS(p))

# Return natural value of a number 
NVALUE = CDR

# Return s a number opossit to a signed
NEG = lambda p: SIGNED(NOT(ISPOS(p)))(NVALUE(p))

##########################
# Arithmetic
##########################

SADD = lambda a: lambda b: (
  XNOR(ISPOS(a))(ISPOS(b)) #if ISPOS(a)==ISPOS(b)
  (CONS(ISPOS(a))(ADD(NVALUE(a))(NVALUE(b)))) # Same sign
  (CONS(XOR(ISPOS(a))(LTE(NVALUE(a))(NVALUE(b))))(DIFF(NVALUE(a))(NVALUE(b)))) # Oposite sign
)
  
SSUB = lambda a: lambda b: SADD(a)(NEG(b))
SMUL = lambda a: lambda b: CONS(XNOR(ISPOS(a))(ISPOS(b)))(MUL(NVALUE(a))(NVALUE(b)))

#POW = lambda a: lambda b: b(a)                  # a ^ b

#SDIV
 
##########################
# Checks
##########################

SISZERO = lambda a: NVALUE(a)(lambda _: FALSE)(TRUE)
#GTE = lambda a: lambda b: ISZERO(SUB(b)(a))
#LTE = lambda a: lambda b: ISZERO(SUB(a)(b))
#GT = lambda a: lambda b: ISZERO(SUB(SUCC(b))(a))
#LT = lambda a: lambda b: ISZERO(SUB(SUCC(a))(b))
#EQ = lambda a: lambda b: AND(GTE(a)(b))(LTE(a)(b))

##########################
# Other
##########################

#MIN = lambda a: lambda b: LTE(a)(b)(a)(b)
#MAX = lambda a: lambda b: GTE(a)(b)(a)(b)

##########################
# Decode Numbers
##########################

def decode_signed(num):
  inc = lambda x: x+1
  value = CDR(num)(inc)(0)
  return CAR(num)(value)(-value)
