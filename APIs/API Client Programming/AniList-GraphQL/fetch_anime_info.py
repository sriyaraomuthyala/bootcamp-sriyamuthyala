import requests
import sys

def get_anime_details(anime_name):
    url = "https://graphql.anilist.co"
    query = """
    {
      Media(search: "%s", type: ANIME) {
        title {
          romaji
        }
        description
        status
      }
    }
    """ % anime_name

    response = requests.post(url, json={'query': query})

    if response.status_code == 200:
        anime = response.json().get("data", {}).get("Media", {})
        if anime:
            title = anime.get('title', {}).get('romaji', 'N/A')
            status = anime.get('status', 'N/A')
            description = anime.get('description', 'No description available.')
            # Removing HTML tags from description (Anilist API includes some)
            clean_description = description.replace("<br>", "\n").replace("<i>", "").replace("</i>", "")

            print(f"Title: {title}")
            print(f"Status: {status}")
            print(f"Description: {clean_description}")
        else:
            print("Anime not found.")
    else:
        print("Failed to fetch anime data.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <ANIME_NAME>")
    else:
        get_anime_details(sys.argv[1])
