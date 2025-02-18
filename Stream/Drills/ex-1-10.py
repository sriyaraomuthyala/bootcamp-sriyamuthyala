from ex_1_8 import efficient_file_processing
def advanced_stream_processing(input_files, output_file, keyword, process_func):
    try:
        with open(output_file, 'w') as out_file:
            for filename in input_files:
                for processed_line in efficient_file_processing(filename, keyword, process_func):
                    out_file.write(str(processed_line) + "\n")
    except Exception as e:
        print(f"Error in processing: {e}")

if __name__ == "__main__":
    input_files = ["sample.txt", "sample2.txt"]
    output_file = "output.txt"
    keyword = "info"
    advanced_stream_processing(input_files, output_file, keyword, str.upper)
