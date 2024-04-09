#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "MyRedditBot/1.0"}  # Custom User-Agent

    params = {}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print("Invalid subreddit. Please enter a valid subreddit.")
            return None

        data = response.json().get("data", {}).get("children", [])
        if not data:
            return hot_list

        for post in data:
            hot_list.append(post["data"]["title"])

        after = data[-1]["data"]["name"]
        return recurse(subreddit, hot_list, after)
    except requests.RequestException as e:
        print("Error:", e)
        return None


# Example usage:
subreddit = "python"
hot_titles = recurse(subreddit)
if hot_titles is not None:
    print(f"All hot articles in r/{subreddit}:")
    for title in hot_titles:
        print(title)
