import argparse
import yaml
import sys
from typing import Iterator, Callable
from sriya_wf_dynamic.stream_functions import *

# Function lookup table
FUNCTION_MAP = {
    "lowercase": stream_lower_case,
    "uppercase": stream_upper_case,
    "remove_stop_words": stream_remove_stop_words,
    "uk_to_us": stream_uk_to_us,
    "number_the_lines": number_the_lines,
    "coalesce_empty_lines": coalesce_empty_lines,
    "remove_empty_lines": remove_empty_lines,
    "remove_even_lines": remove_even_lines,
    "break_lines": break_lines
}

def apply_pipeline(stream: Iterator[str], functions: list[str]) -> Iterator[str]:
    """Apply a sequence of functions from YAML pipeline to a text stream."""
    for func_name in functions:
        if func_name in FUNCTION_MAP:
            stream = FUNCTION_MAP[func_name](stream)
        else:
            print(f"Warning: Function {func_name} not found.")
    return stream

def main():
    parser = argparse.ArgumentParser(description="Process streaming text using a YAML pipeline.")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("config_file", help="Path to the YAML pipeline configuration")
    parser.add_argument("-o", "--output", help="Output file name (default: output.txt)", default="output.txt")

    args = parser.parse_args()

    # Load pipeline configuration
    with open(args.config_file, "r") as yaml_file:
        config = yaml.safe_load(yaml_file)

    pipeline_functions = config.get("pipeline", [])

    # Read input, apply pipeline, and write output
    with open(args.input_file, "r") as infile, open(args.output, "w") as outfile:
        processed_stream = apply_pipeline(infile, pipeline_functions)
        outfile.writelines(processed_stream)

if __name__ == "__main__":
    main()
