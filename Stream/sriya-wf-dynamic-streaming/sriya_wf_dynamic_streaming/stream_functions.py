def upper_case(text: str) -> str:
    return text.upper()
def capitalize(text: str) -> str:
    """Capitalize the first letter of each word in a sentence and ensure a newline at the end."""
    return " ".join(word.capitalize() for word in text.split()) + "\n"

