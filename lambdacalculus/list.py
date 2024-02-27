from .bool import TRUE, FALSE
from .bool import OR, NOT
from .natural import GTE, ISZERO
from .natural import SUCC, PRED
from .natural import ZERO
from .pair import CONS, CAR, CDR
from .combinators import Y

##########################
# List
##########################

LIST = CONS(TRUE)(TRUE) # Create new list
EMPTY = lambda list: CAR(list)
HEAD = lambda list: CAR(CDR(list))
TAIL = lambda list: CDR(CDR(list))

##########################

PREPEND = lambda list: lambda x: CONS(FALSE)(CONS(x)(list))
APPEND = Y(
  lambda f: lambda list: lambda x: EMPTY(list)
  (lambda _: PREPEND(list)(x))
  (lambda _: CONS(FALSE)(CONS(HEAD(list))(f(TAIL(list))(x))))
  (TRUE)
)

##########################

REVERSE = Y(
  lambda f: lambda list: EMPTY(list)
  (lambda _: LIST)
  (lambda _: APPEND(f(TAIL(list)))(HEAD(list)))
  (TRUE)
)

# MAP - apply `a` function to every element on the list. Result a new list 
MAP = Y(
  lambda f: lambda a: lambda list: EMPTY(list)
  (lambda _: LIST)
  (lambda _: PREPEND(f(a)(TAIL(list)))(a(HEAD(list))))
  (TRUE)
)

##########################
# Special list creation 
##########################

# RANGE start, end
RANGE = Y(
  lambda f: lambda a: lambda b: GTE(a)(b) # a >= b
  (lambda _: LIST)
  (lambda _: PREPEND(f(SUCC(a))(b))(a))
  (TRUE)
)

# REDUCE r, list, v
# r - xs, x - function element, value -> new value
# list
# v - initial value 
REDUCE = FOLD = Y(
  lambda f: lambda r: lambda list: lambda v: EMPTY(list)  #if list is empty
  (lambda _: v)                                           #return accumulated value v
  (lambda _: f(r)(TAIL(list))(r(HEAD(list))(v)))          #call it self on TAIL with updated accumulated value += r(element)(v)
  (TRUE)
)

# FILTER f, list
# f predicate to keep given element in resulting list
# list 
FILTER = lambda f: lambda list: (
  REDUCE
  (lambda x: lambda xs: f(x)(APPEND(xs)(x))(xs)) # if f(x) ?  ADDEND(xs)(x) : xs
  (list)
  (LIST)
)

# DROP
# n - number of elements to drop from begining
# list
DROP = lambda n: lambda list: n(TAIL)(list)

# TAKE
# n - number of element to take from begining
TAKE = Y(
  lambda f: lambda n: lambda list: OR(EMPTY(list))(ISZERO(n)) # if list is already empty or n==0
  (lambda _: LIST)                                            # new list
  (lambda _: (PREPEND(f(PRED(n))(TAIL(list)))(HEAD(list))) )
  (TRUE)
)

LENGTH = lambda list: REDUCE(lambda x: lambda n: SUCC(n))(list)(ZERO)

# INDEX n list - get n-th element from list
INDEX = Y(
  lambda f: lambda n: lambda list: ISZERO(n) # if n==0
  (lambda _: HEAD(list))                     # HEAD(list)
  (lambda _: f(PRED(n))(TAIL(list)))
  (TRUE)  
)

# ANY list - check if any element is true
ANY = Y(
  lambda f: lambda list: EMPTY(list)
  (lambda _: FALSE)
  (lambda _: HEAD(list)(TRUE)(f(TAIL(list))))
  (TRUE)  
)

# ALL list - checks if all elements are true
ALL = Y(
  lambda f: lambda list: EMPTY(list)
  (lambda _: TRUE)
  (lambda _: NOT(HEAD(list))(FALSE)(f(TAIL(list))))
  (TRUE)
)

##########################
# Debug list 
##########################
def decode_list(list,limit):
  decoded = []
  for _ in range(limit):
    if EMPTY(list) is TRUE:
      return decoded
    decoded.append(HEAD(list))
    list = TAIL(list)
  raise RuntimeError(f"List is longer than provided limit {limit}")
  
