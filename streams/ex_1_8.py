from ex_1_4 import filtered_file_generator
def efficient_file_processing(filename, keyword, process_func):
    for line in filtered_file_generator(filename, keyword):
        yield process_func(line)

if __name__ == "__main__":
    filename = "large_sample.txt"
    keyword = "data"
    for result in efficient_file_processing(filename, keyword, str.upper):
        print(result)
