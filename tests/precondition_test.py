import conker
from nose.tools import assert_raises, assert_equals


##############################


@conker.pre("n >= 0")
def square_root(n):
    import math
    return math.sqrt(n)


@conker.pre("name != ''")
def greet(name):
    return f"Hello, {name}!"


@conker.pre("x != 0")
def add(x, y):
    return x + y


@conker.pre("y != 9")
def subtract(x, y):
    return x - y


@conker.pre(
    "x >= -1",
    "x <= 1",
)
def arcsin(x):
    import math
    return math.asin(x)


@conker.pre(
    "text != ''"
)
def shout(text=""):
    pass


##############################


def test_preconditions_fail():
    data = [
        (square_root, [-1]),
        (square_root, [-2]),
        (greet,       [""]),
        (add,         [0, 1]),
        (subtract,    [5, 9]),
        (arcsin,      [2]),
        (arcsin,      [-2]),
        (arcsin,      [1.1]),
    ]
    for function, args in data:
        yield (assert_raises, conker.ConkerError, function, *args)

    yield assert_raises, conker.ConkerError, lambda: shout(text="")
    yield assert_raises, conker.ConkerError, lambda: shout()
    

def test_functions_run_correctly():
    data = [
        (square_root, [9],  3),
        (square_root, [16], 4),
        (square_root, [25], 5),

        (greet, ["World"], "Hello, World!"),
        (greet, ["Byxor"], "Hello, Byxor!"),

        (add, [10, 20], 30),
        (add, [50, 10], 60),

        (subtract, [20, 10], 10),
        (subtract, [50, 50], 0),

        (arcsin, [0],  0),
    ]
    for function, args, expected in data:
        yield assert_equals, expected, function(*args)
