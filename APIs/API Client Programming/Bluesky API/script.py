from atproto import Client
import sys

# Replace with your Bluesky credentials
USERNAME = "hellosriyahere.bsky.social"  # Example: "yourname.bsky.social"
APP_PASSWORD = "ggmx-nr6i-6rdi-g77m"  # From Bluesky App Passwords

def post_to_bluesky(message):
    try:
        client = Client()
        client.login(USERNAME, APP_PASSWORD)  # Log in to get session token
        
        client.send_post(message)  # Send the post
        print(f"Posted successfully: {message}")

    except Exception as e:
        print(f"Error posting to Bluesky: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py \"Your message here\"")
    else:
        post_to_bluesky(sys.argv[1])
