# processing_functions.py

import re
import requests
import os

def process_file(input_filename, output_filename, process_function):
    """Helper function to process a file and write output."""
    if output_filename is None:
        output_filename = f"{input_filename}.processed"

    with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
        for line in infile:
            outfile.write(process_function(line))

def upper_case(input_filename, output_filename=None):
    """Convert file content to uppercase."""
    process_file(input_filename, output_filename, str.upper)

def lower_case(input_filename, output_filename=None):
    """Convert file content to lowercase."""
    process_file(input_filename, output_filename, str.lower)

def capitalize(input_filename, output_filename=None):
    """Capitalize the first letter of each word in the file."""
    process_file(input_filename, output_filename, str.title)

def remove_stop_words(input_filename, output_filename=None):
    """Remove stop words from the file content."""
    stop_words = {"a", "an", "the", "and", "or"}

    if output_filename is None:
        output_filename = f"{input_filename}.processed"

    with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
        for line in infile:
            words = line.split()
            filtered_words = [word for word in words if word.lower() not in stop_words]
            outfile.write(" ".join(filtered_words) + "\n")

def fetch_geo_ip(ip):
    """Fetch geolocation details for an IP address."""
    response = requests.get(f"https://ipinfo.io/{ip}/geo")
    if response.status_code == 200:
        data = response.json()
        return f"{data.get('city', '')}, {data.get('region', '')}, {data.get('country', '')}"
    return "Unknown Location"

def uk_to_us(input_filename, output_filename=None):
    """Convert UK spellings to US spellings."""
    uk_to_us_dict = {
        r"(\b)colour(\b)": r"\1color\2",
        r"(\b)favourite(\b)": r"\1favorite\2",
        r"(\b)organisation(\b)": r"\1organization\2",
        r"sation\b": r"zation"
    }

    if output_filename is None:
        output_filename = f"{input_filename}.processed"

    with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
        for line in infile:
            for uk, us in uk_to_us_dict.items():
                line = re.sub(uk, us, line)
            outfile.write(line)
