#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}  # Custom User-Agent
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException as e:
        print("Error:", e)
        return 0


# Example usage:
subreddit = "python"
print(f"The number of subscribers in r/{subreddit} is:",
      number_of_subscribers(subreddit))
