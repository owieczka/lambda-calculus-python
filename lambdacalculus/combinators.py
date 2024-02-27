from .bool import TRUE, IDENTYTY

##########################
# Combinators
##########################

I = IDENTYTY # I:: a -> a
K = TRUE     # K:: a -> b -> a
S = lambda f: lambda g: lambda x: f(x)(g(x)) # ??S:: (a -> b -> c) -> (a -> b) -> a -> c 
Y = lambda f: (
  (lambda x: f(lambda y: x(x)(y)))
  (lambda x: f(lambda y: x(x)(y)))
)

# Y(
#  lambda f: .... <condition>
# (lambda _: ....) # True condition - recursion end
# (lambda _: ....) # False condition - recursion call to f
# (ZERO)
# )
