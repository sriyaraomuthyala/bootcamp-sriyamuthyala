import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)

if response.status_code == 200:
    top_stories = response.json()[:5]
    for story_id in top_stories:
        story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json").json()
        print(f"Title: {story['title']}, URL: {story.get('url', 'N/A')}")
else:
    print("Failed to fetch Hacker News posts")
