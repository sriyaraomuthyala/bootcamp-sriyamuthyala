import argparse
import yaml
from sriya_wf_dynamic_streaming.stream_adapter_functions import FUNCTION_MAP

def process_pipeline(input_stream, config_file):
    """Applies a sequence of transformations defined in a YAML config file."""
    with open(config_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    functions = config.get("pipeline", [])

    for func_name in functions:
        if func_name in FUNCTION_MAP:
            input_stream = FUNCTION_MAP[func_name](input_stream)
        else:
            raise ValueError(f"Function {func_name} not found in FUNCTION_MAP")

    return input_stream

def main():
    parser = argparse.ArgumentParser(description="Process streaming text using a YAML pipeline.")
    parser.add_argument("input_file", type=str, help="Path to the input text file")
    parser.add_argument("config_file", type=str, help="Path to the YAML pipeline configuration")
    parser.add_argument("-o", "--output", type=str, default="output.txt", help="Output file name (default: output.txt)")

    args = parser.parse_args()

    # Read input file
    with open(args.input_file, "r", encoding="utf-8") as f:
        input_data = f.readlines()

    # Process the pipeline
    output_data = process_pipeline(input_data, args.config_file)

    # Write output to file
    with open(args.output, "w", encoding="utf-8") as f:
        f.writelines(output_data)

    print(f"Pipeline processed. Output saved to {args.output}")

if __name__ == "__main__":
    main()
