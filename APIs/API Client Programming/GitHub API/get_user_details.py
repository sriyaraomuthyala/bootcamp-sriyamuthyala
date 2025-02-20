import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <GitHub_Username>")
    sys.exit(1)

username = sys.argv[1]
url = f"https://api.github.com/users/{username}"
response = requests.get(url)

if response.status_code == 200:
    user = response.json()
    print(f"Name: {user.get('name', 'N/A')}")
    print(f"Public Repos: {user.get('public_repos', 'N/A')}")
else:
    print("User not found")
