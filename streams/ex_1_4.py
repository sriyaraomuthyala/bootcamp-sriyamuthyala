from ex_1_3 import file_generator
def filtered_file_generator(filename, keyword):
    for line in file_generator(filename):
        if keyword in line:
            yield line

if __name__ == "__main__":
    filename = "sample.txt"
    keyword = "important"
    for line in filtered_file_generator(filename, keyword):
        print(line)

