#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if after:
        url = \
            "https://www.reddit.com/r/" \
            "{}/hot.json?limit=100&after={}".format(subreddit, after)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = \
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)"}

    request = requests.get(url, headers=header)

    if request.status_code != 200:
        return None

    if request.status_code == 200:
        data = request.json().get("data").get("children")
        after = request.json().get("data").get("after")

        if data is None:
            return None

        for children in data:
            tit = children.get("data").get("title")
            hot_list.append(tit)

    if after:
        recurse("{}".format(subreddit), after=after)
    return hot_list
