import requests

url = "https://spacex-production.up.railway.app/graphql/"
query = """
{
  launchesPast(limit: 5) {
    mission_name
    launch_date_utc
    rocket {
      rocket_name
    }
  }
}
"""

response = requests.post(url, json={'query': query})

if response.status_code == 200:
    launches = response.json()["data"]["launchesPast"]
    for launch in launches:
        print(f"Mission: {launch['mission_name']}, Rocket: {launch['rocket']['rocket_name']}, Date: {launch['launch_date_utc']}")
else:
    print("Failed to fetch launch data")
