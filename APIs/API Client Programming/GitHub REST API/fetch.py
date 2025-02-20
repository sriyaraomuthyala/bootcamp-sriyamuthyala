import requests
import sys

# (Optional) Add your GitHub token for higher request limits
GITHUB_TOKEN = "your_github_token"  # Replace with your GitHub token or set to None
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

def get_github_contributions(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        events = response.json()
        contributions = sum(1 for event in events if event["type"] in ["PushEvent", "PullRequestEvent"])

        print(f"{username} has made {contributions} contributions in the last year.")
    else:
        print("Failed to fetch contributions. Check the username or API rate limits.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <GITHUB_USERNAME>")
    else:
        get_github_contributions(sys.argv[1])
