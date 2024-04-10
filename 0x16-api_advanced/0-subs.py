#!/usr/bin/python3
"""Queries subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print("Error:", e)
        return 0

# Example usage:
subreddit = "python"
print(f"Number of subscribers in r/{subreddit}:
      {number_of_subscribers(subreddit)}")
