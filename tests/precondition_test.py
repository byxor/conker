import conker
from nose.tools import assert_raises


@conker.pre("n >= 0")
def square_root(n):
    pass


def test_precondition_fails():
    yield assert_raises, conker.ConkerError, square_root, -1
    
