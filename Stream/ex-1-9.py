from ex_1_6 import file_pipeline
def safe_file_pipeline(filename, keyword):
    try:
        for line in file_pipeline(filename, keyword):
            yield line
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    filename = "sample.txt"
    keyword = "error"
    for result in safe_file_pipeline(filename, keyword):
        print(result)
