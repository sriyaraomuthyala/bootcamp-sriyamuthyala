import itertools
def process_iterator(iterator, func):
    for item in iterator:
        yield func(item)

if __name__ == "__main__":
    for num in process_iterator(range(1, 6), lambda x: x * 2):
        print(num)
