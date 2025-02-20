import requests

url = "https://rickandmortyapi.com/api/character"
response = requests.get(url)

if response.status_code == 200:
    characters = response.json()["results"][:5]
    for char in characters:
        print(f"Name: {char['name']}, Species: {char['species']}")
else:
    print("Failed to fetch characters")
