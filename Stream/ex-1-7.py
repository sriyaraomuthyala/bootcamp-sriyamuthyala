import itertools

def chained_iterators(*iterables):
    return itertools.chain(*iterables)

if __name__ == "__main__":
    for num in chained_iterators(range(1, 4), range(4, 7)):
        print(num)
