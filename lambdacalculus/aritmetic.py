from .bool import NOT
from .natural import ISZERO, LTE, LT
from .natural import ZERO, ONE, TWO
from .natural import SUCC, PRED, MUL, ADD, SUB
from .combinators import Y

##########################
# ARITMETIC
##########################

# Factorial n! = n * (n-1) * (n-2) * ... * 1
FAC = Y(
  lambda f: lambda n: ISZERO(n)  # n==0
  (lambda _: ONE)                # 1
  (lambda _: MUL(n)(f(PRED(n)))) # n * f(n-1)
  (ZERO)
)

# Fibonaci fib(n) = fib(n-1) + fib(n-2)
FIB = Y(
  lambda f: lambda n: LTE(n)(TWO)               # n<= 2
  (lambda _: ONE)                               # 1
  (lambda _: ADD(f(PRED(n)))(f(PRED(PRED(n))))) # f(n-1) + f(n-2)
  (ZERO)
)

# Division a / b
DIV = Y(
  lambda f: lambda a: lambda b: LT(a)(b) # a < b
  (lambda _: ZERO)                       # 0
  (lambda _: SUCC(f(SUB(a)(b))(b)))      # f(a-b, b) + 1
  (ZERO)
)

# Modulus - reminder of division a % b
MOD = Y(
  lambda f: lambda a: lambda b: LT(a)(b) # a < b
  (lambda _: a)                          # a
  (lambda _: f(SUB(a)(b))(b))            # f(a-b, b)
  (ZERO)
)

EVEN = lambda n: ISZERO(MOD(n)(TWO))
ODD  = lambda n: NOT(EVEN(n))
