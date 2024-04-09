#!/usr/bin/python3
"""This function queries subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """The total number of subscribers on a given subreddit is returned."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0
        data = response.json().get("data")
        return data.get("subscribers")
    except requests.RequestException as e:
        print("Error:", e)
        return 0


# Example of usage:
subreddit = "python"
print(f"The number of subscribers in r/{subreddit} is:",
      number_of_subscribers(subreddit))
