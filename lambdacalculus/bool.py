##########################
IDENTYTY = lambda a: a
IF = IDENTYTY

##########################
# Boolean values
##########################
TRUE = lambda t: lambda f: t
TRUE.__name__ = "TRUE"

FALSE = lambda t: lambda f: f
FALSE.__name__ = "FALSE"
 
##########################
# Boolean operations
##########################
NOT = lambda x: x(FALSE)(TRUE)
AND = lambda x: lambda y: x(y)(x)
OR = lambda x: lambda y: x(x)(y)

XOR = lambda x: lambda y: x(NOT(y))(y)
XNOR = lambda x: lambda y: NOT(XOR(x)(y))
NAND = lambda x: lambda y: NOT(AND(x)(y))
NOR = lambda x: lambda y: NOT(OR(x)(y))

def showLogic(x):
  return x('true')('false')
##########################
