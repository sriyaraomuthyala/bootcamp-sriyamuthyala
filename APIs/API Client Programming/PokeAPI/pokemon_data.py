import requests
import sys

def get_pokemon_details(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()
        types = [t["type"]["name"] for t in pokemon["types"]]
        print(f"Pokémon: {pokemon_name.capitalize()}, Types: {', '.join(types)}")
    else:
        print("Pokémon not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <POKEMON_NAME>")
    else:
        get_pokemon_details(sys.argv[1])
