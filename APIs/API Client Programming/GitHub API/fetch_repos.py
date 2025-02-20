import requests

url = "https://api.github.com/repositories"
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    for repo in repos[:10]:  # Fetch first 10 repos
        print(repo['name'])
else:
    print("Failed to fetch repositories")
