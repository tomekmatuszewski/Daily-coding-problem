# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
# last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    return lambda f: f(a, b)


# Implement car and cdr.


def car(func):
    new_f = lambda x, y: x
    return func(new_f)


def cdr(func):
    new_f = lambda x, y: y
    return func(new_f)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4

print(cons(2,3)(lambda x,y: x+y))