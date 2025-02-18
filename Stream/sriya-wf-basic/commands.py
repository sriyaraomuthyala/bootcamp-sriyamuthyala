# commands.py

import typer
from processing_functions import upper_case, lower_case, capitalize, remove_stop_words, fetch_geo_ip, uk_to_us

app = typer.Typer()

@app.command()
def uppercase(input_file: str, output_file: str = None):
    """Convert file contents to uppercase."""
    upper_case(input_file, output_file)
    print(f"Processed file saved as: {output_file or input_file + '.processed'}")

@app.command()
def lowercase(input_file: str, output_file: str = None):
    """Convert file contents to lowercase."""
    lower_case(input_file, output_file)
    print(f"Processed file saved as: {output_file or input_file + '.processed'}")

@app.command()
def capitalize_words(input_file: str, output_file: str = None):
    """Capitalize the words in the file."""
    capitalize(input_file, output_file)
    print(f"Processed file saved as: {output_file or input_file + '.processed'}")

@app.command()
def remove_stopwords(input_file: str, output_file: str = None):
    """Remove common stopwords from the file."""
    remove_stop_words(input_file, output_file)
    print(f"Processed file saved as: {output_file or input_file + '.processed'}")

@app.command()
def geo_ip(ip: str):
    """Fetch geolocation details of an IP."""
    print(fetch_geo_ip(ip))

@app.command()
def convert_uk_to_us(input_file: str, output_file: str = None):
    """Convert UK spellings to US spellings in the file."""
    uk_to_us(input_file, output_file)
    print(f"Processed file saved as: {output_file or input_file + '.processed'}")

def main():
    app()

if __name__ == "__main__":
    main()
