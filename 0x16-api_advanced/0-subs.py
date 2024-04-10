#!/usr/bin/python3
"""This function queries subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


# Example usage:
subreddit = "python"
print(f"Number of subscribers in r/{subreddit}:
      {number_of_subscribers(subreddit)}")
