import conker
from nose.tools import assert_raises, assert_equals


@conker.pre("n >= 0")
def square_root(n):
    import math
    return math.sqrt(n)


def test_precondition_fails():
    yield assert_raises, conker.ConkerError, square_root, -1
    

def test_function_runs_correctly():
    data = [
        (9,  3),
        (16, 4),
        (25, 5),
    ]
    for n, expected in data:
        yield assert_equals, expected, square_root(n)
    
