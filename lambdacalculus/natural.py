from .bool import TRUE, FALSE, IDENTYTY, AND

##########################
# Arithmetic
##########################

SUCC = lambda n: lambda f: lambda x: f(n(f)(x)) # n + 1
ADD = lambda a: lambda b: b(SUCC)(a)            # a + b
MUL = lambda a: lambda b: lambda f: b(a(f))     # a * b
POW = lambda a: lambda b: b(a)                  # a ^ b

PRED = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda _: x)(IDENTYTY) # n - 1
SUB = lambda a: lambda b: b(PRED)(a)            # a - b
DIFF = lambda a: lambda b: ADD(SUB(a)(b))(SUB(b)(a))
 
##########################
# Numbers
##########################
ZERO = FALSE # lambda f: lambda x: x
ZERO.__name__ = "ZERO"
ONE = IDENTYTY # lambda f: lambda x: f(x)
ONE.__name__ = "ONE"
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = SUCC(THREE)   # lambda f: lambda x: f(f(f(f(x))))
FIVE = ADD(TWO)(THREE) # lambda f: lambda x: f(f(f(f(f(x)))))
SIX = MUL(TWO)(THREE)  # lambda f: lambda x: f(f(f(f(f(f(x))))))
SEVEN = SUCC(SIX)
EIGHT = MUL(FOUR)(TWO)
NINE = POW(THREE)(TWO)
TEN = MUL(FIVE)(TWO)

##########################
# Checks
##########################

ISZERO = lambda a: a(lambda _: FALSE)(TRUE)
GTE = lambda a: lambda b: ISZERO(SUB(b)(a))
LTE = lambda a: lambda b: ISZERO(SUB(a)(b))        
GT = lambda a: lambda b: ISZERO(SUB(SUCC(b))(a))   # b>a
LT = lambda a: lambda b: ISZERO(SUB(SUCC(a))(b))   # a<b
EQ = lambda a: lambda b: AND(GTE(a)(b))(LTE(a)(b)) # a==b

##########################
# Other
##########################

MIN = lambda a: lambda b: LTE(a)(b)(a)(b)
MAX = lambda a: lambda b: GTE(a)(b)(a)(b)

##########################
# Decode Numbers
##########################

def decode_natural(num):
  inc = lambda x: x+1
  return num(inc)(0)

#LAZY_TRUE = lambda x: lambda y: x()
#LAZY_FALSE = lambda x: lambda y: y()

#LAZY_ISZERO = lambda n: n(lambda f: LAZY_FALSE)(LAZY_TRUE)
