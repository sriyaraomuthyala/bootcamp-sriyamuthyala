from typing import Iterator

STOP_WORDS = {"the", "is", "in", "and", "of", "a", "to"}

UK_US_MAP = {
    "colour": "color",
    "favourite": "favorite",
    "honour": "honor",
    "realise": "realize"
}

def stream_lower_case(stream: Iterator[str]) -> Iterator[str]:
    """Convert text to lowercase."""
    for line in stream:
        yield line.lower()

def stream_upper_case(stream: Iterator[str]) -> Iterator[str]:
    """Convert text to uppercase."""
    for line in stream:
        yield line.upper()

def stream_remove_stop_words(stream: Iterator[str]) -> Iterator[str]:
    """Remove stop words from text."""
    for line in stream:
        yield " ".join(word for word in line.split() if word.lower() not in STOP_WORDS) + "\n"

def stream_uk_to_us(stream: Iterator[str]) -> Iterator[str]:
    """Convert UK spellings to US spellings."""
    for line in stream:
        for uk, us in UK_US_MAP.items():
            line = line.replace(uk, us)
        yield line

def number_the_lines(stream: Iterator[str]) -> Iterator[str]:
    """Add line numbers to each line."""
    for i, line in enumerate(stream, start=1):
        yield f"{i}: {line.strip()}\n"

def coalesce_empty_lines(stream: Iterator[str]) -> Iterator[str]:
    """Remove multiple empty lines, leaving just one."""
    prev_empty = False
    for line in stream:
        if line.strip() == "":
            if not prev_empty:
                yield "\n"
                prev_empty = True
        else:
            yield line
            prev_empty = False

def remove_empty_lines(stream: Iterator[str]) -> Iterator[str]:
    """Remove all empty lines."""
    for line in stream:
        if line.strip():
            yield line

def remove_even_lines(stream: Iterator[str]) -> Iterator[str]:
    """Remove all even-numbered lines."""
    for i, line in enumerate(stream, start=1):
        if i % 2 != 0:
            yield line

def break_lines(stream: Iterator[str], length: int = 20) -> Iterator[str]:
    """Break long lines into shorter lines."""
    for line in stream:
        words = line.strip().split()
        new_line = []
        char_count = 0
        for word in words:
            if char_count + len(word) > length:
                yield " ".join(new_line) + "\n"
                new_line = []
                char_count = 0
            new_line.append(word)
            char_count += len(word) + 1
        if new_line:
            yield " ".join(new_line) + "\n"
