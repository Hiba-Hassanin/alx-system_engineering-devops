#!/usr/bin/python3
"""
This script queries the Reddit API and prints
the titles of the first 10 hot posts
for a given subreddit. If the subreddit
is not valid, it prints 'None'.
"""
import requests

import requests


def number_of_subscribers(subreddit):
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (0)
    response = response.json()
    if 'data' in response:
        return (response.get('data').get('subscribers'))

    else:
        return (0)
