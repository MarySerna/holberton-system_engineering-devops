#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns
the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0"}
    request = requests.get(url, headers=header)

    if request.status_code == 200:
        data = request.json().get("data")
        subs = data.get("subscribers")
        return subs
    else:
        return 0
