from .bool import TRUE, FALSE

##########################
# Pair
##########################

CONS = lambda a: lambda b: lambda s: s(a)(b)

CAR = lambda p: p(TRUE)
CDR = lambda p: p(FALSE)

