import conker
from nose.tools import assert_raises, assert_equals


@conker.pre("n >= 0")
def square_root(n):
    import math
    return math.sqrt(n)


@conker.pre("target != ''")
def greet(target):
    return f"Hello, {target}!"


def test_precondition_fails():
    yield assert_raises, conker.ConkerError, square_root, -1
    yield assert_raises, conker.ConkerError, greet, ""
    

def test_functions_run_correctly():
    data = [
        (square_root, [9],  3),
        (square_root, [16], 4),
        (square_root, [25], 5),

        (greet, ["World"], "Hello, World!"),
        (greet, ["Byxor"], "Hello, Byxor!"),
    ]
    for function, args, expected in data:
        yield assert_equals, expected, function(*args)
    
