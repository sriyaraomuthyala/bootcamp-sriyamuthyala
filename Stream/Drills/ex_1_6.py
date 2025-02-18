import itertools
from ex_1_4 import filtered_file_generator
def file_pipeline(filename, keyword):
    for line in filtered_file_generator(filename, keyword):
        yield len(line.split())  # Counts words in line

if __name__ == "__main__":
    filename = "sample.txt"
    keyword = "important"
    for count in file_pipeline(filename, keyword):
        print(count)
