from functools import partial, reduce, total_ordering

def multiply(x, y):
    return x * y

double = partial(multiply, 2)

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
