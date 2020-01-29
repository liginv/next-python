""" 
Using asset as a debugging aid.
It do nothing if the statement is right,
but if it is not, throw an AssertionError.

It is use to inform developer about unrecoverable errors in a program.
They declare some conditions are impossible in your code.

Syntax:
assert expression1 ["," expression2]
[] => optional
expression1 => condition we test
expression2 => error message that displays if the assertion fails.

Caveat#1 
    Never use for DATA VALIDATION
    Asserts can be globally disabled by with an interpreter settings.

Caveat#2 
    When pass a tuple as first argument(expression1), assertion always evaluates as true.
    non-empty tuples always being truthy in python.

    assert (1 == 2, 'This is not true')  ==> Wrong (always true)
    assert 1 == 2, 'This is not true' ==> Right
"""


def discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price
