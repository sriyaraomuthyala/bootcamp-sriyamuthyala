from typing import Callable, Iterator

# Type Aliases
StringFunction = Callable[[str], str]
StreamFunction = Callable[[Iterator[str]], Iterator[str]]

def string_to_stream_function(in_function: StringFunction) -> StreamFunction:
    """Convert a string function to a streaming function."""
    def stream_function(text_stream: Iterator[str]) -> Iterator[str]:
        for line in text_stream:
            yield in_function(line)
    return stream_function

# Import string functions
from sriya_wf_dynamic_streaming.stream_functions import upper_case, capitalize

# Convert them to stream functions
stream_upper_case = string_to_stream_function(upper_case)
stream_capitalize = string_to_stream_function(capitalize)

# Function lookup dictionary
FUNCTION_MAP = {
    "coalesce_empty_lines": lambda stream: (line for line in stream if line.strip()),
    "break_lines": lambda stream: (line.replace(". ", ".\n") for line in stream),
    "number_the_lines": lambda stream: (f"{i+1}: {line}" for i, line in enumerate(stream)),
    "stream_capitalize": stream_capitalize,
    "stream_upper_case": stream_upper_case
}
