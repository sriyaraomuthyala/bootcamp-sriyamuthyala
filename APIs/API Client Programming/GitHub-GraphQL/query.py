import requests
import sys

# Replace with your GitHub token
GITHUB_TOKEN = "ghp_3Y14K3NskAMLtbAPbhqTcfp4FQrgLy3s"

def get_github_repos(username):
    url = "https://api.github.com/graphql"
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    query = f"""
    {{
      user(login: "{username}") {{
        repositories(first: 5) {{
          nodes {{
            name
            description
          }}
        }}
      }}
    }}
    """
    
    response = requests.post(url, json={'query': query}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        repos = data.get("data", {}).get("user", {}).get("repositories", {}).get("nodes", [])
        
        if repos:
            for repo in repos:
                print(f"Repo: {repo['name']}, Description: {repo.get('description', 'No description')}")
        else:
            print("No repositories found.")
    else:
        print("Failed to fetch repositories. Check your token and username.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <GITHUB_USERNAME>")
    else:
        get_github_repos(sys.argv[1])
