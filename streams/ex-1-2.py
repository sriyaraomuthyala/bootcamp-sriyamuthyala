# Custom Iterator for File Reading: Reads a file line by line
class FileIterator:
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line.strip()

if __name__ == "__main__":
    filename = "sample.txt"  # Replace with an actual file
    for line in FileIterator(filename):
        print(line)
