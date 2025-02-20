import requests

API_KEY = "BAdOEwW4jZOBMw0FAWEe0UeY7pBhA6XG"
url = f"https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    books = response.json()["results"]["books"]
    for book in books[:5]:
        print(f"Title: {book['title']}, Author: {book['author']}")
else:
    print("Failed to fetch NYT Best Sellers")
