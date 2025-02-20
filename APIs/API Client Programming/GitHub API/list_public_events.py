import requests

url = "https://api.github.com/events"
response = requests.get(url)

if response.status_code == 200:
    events = response.json()
    for event in events[:5]:  # Fetch first 5 events
        print(f"Event: {event['type']} by {event['actor']['login']}")
else:
    print("Failed to fetch events")
