# lambda-calculus-python

1. Boolean operation - [bool](lambdacalculus/bool.py) 
2. Natural numbers - [natural](lambdacalculus/natural.py)
3. Combinators - [combinators](lambdacalculuc/combinators.py)
4. More aritmetics - [arithmetic](lambdacalculuc/arithmetic.py)
5. Signed numbers - [signed](lambdacalculus/signed.py)
6. Lists - [list](lambdacalculu/list.py)

# Naturals

Numbers definitions
```
ZERO = f -> x -> x

ONE  = f -> x -> f(x)

TWO  = f -> x -> f(f(x))
```

Next number 
```
SUCC = n -> f -> x -> f(n(f)(x))

SUCC(ZERO) = 
= (n -> f -> x -> f(n(f)(x)))(f -> x -> x) =
= (f -> x -> f((f -> x -> x)(f)(x))) =
= f -> x -> f(x)
= ONE


SUCC(ONE) = 
= (n -> f -> x -> f(n(f)(x)))(f -> x -> f(x)) =
= f -> x -> f((f -> x -> f(x))(f)(x)) =
= f -> x -> f((x -> f(x))(x)) =
= f -> x -> f(f(x))
= TWO
```

Previous number

```
PRED = n -> f -> x -> n(g -> h-> h(g(f)))(a -> x)(IDENTYTY)

PRED(ZERO) = 
= (n -> f -> x -> n(g -> h-> h(g(f)))(a -> x)(IDENTYTY))(f -> x -> x) =
= f -> x -> (f -> x -> x)(g -> h-> h(g(f)))(x) =
= f -> x -> x =
ZERO

PRED(ONE) = 
= (n -> f -> x -> n(g -> h-> h(g(f)))(a -> x)(IDENTYTY))(f -> x -> f(x)) =
= (f -> x -> (f -> x -> f(x))(g -> h-> h(g(f)))(a -> x)(IDENTYTY)) =
= f -> x -> (x -> (g -> h-> h(g(f)))(x))(a -> x)(IDENTYTY) =
= f -> x -> (x -> (h-> h(x(f))))(a -> x)(IDENTYTY) =
= f -> x -> ((h-> h((a -> x)(f))))(IDENTYTY) =
= f -> x -> ((h-> h((x))))(IDENTYTY) =
= f -> x -> (h-> h(x))(IDENTYTY) =
= f -> x -> (IDENTYTY(x)) =
= f -> x -> (x) =
= f -> x -> x =
ZERO

PRED(TWO) = 
= (n -> f -> x -> n(g -> h-> h(g(f)))(a -> x)(IDENTYTY))(f -> x -> f(f(x))) =
= (f -> x -> (f -> x -> f(f(x)))(g -> h-> h(g(f)))(a -> x)(IDENTYTY)) =
= (f -> x -> (x -> (g -> h-> h(g(f)))((g -> h-> h(g(f)))(x)))(a -> x)(IDENTYTY)) =
= (f -> x -> (x -> (g -> h-> h(g(f)))((h-> h(x(f)))))(a -> x)(IDENTYTY)) =
= (f -> x -> (x -> (h-> h((h1-> h1(x(f)))(f))))(a -> x)(IDENTYTY)) =
= (f -> x -> (x -> (h-> h(f(x(f)))))(a -> x)(IDENTYTY)) =
= (f -> x -> ((h-> h(f(x)))(IDENTYTY)) =
= (f -> x -> (((IDENTYTY)(f(x)))) =
= (f -> x -> (((f(x)))) =
= (f -> x -> f(x)) =
= f -> x -> f(x) =
= ONE
```

# Defininig recursive functions

Recursive functions can be define using Y combinator as folows

```
FUN = Y(
  lambda f: <func params>: <condition>
  (lambda _: <cond_true - end recursion>)
  (lambda _: <cond_false - recursion - call to f>)
  (ZERO)
)
```

For more examples you can examine fibonaci `FIB` or division `DIV` functions

# Signed Numbers

You can create signed number with `SIGNED` function and providing two arguments


DIFF -> ABS_DIFF

python -m cProfile main.py
mypy main.py
pypy3 main.py

# Ideas

- Implement Integrals as pair
- Implement Rationals as pair of Integralas
- Implement Naturals as Binary Numbers - List of Bools

