def file_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

if __name__ == "__main__":
    filename = "sample.txt"
    for line in file_generator(filename):
        print(line)
