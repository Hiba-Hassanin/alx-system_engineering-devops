#!/usr/bin/python3
"""
Queries the Reddit API and returns the
number of subscribers for a given subreddit.
If an invalid subreddit is provided,
the function returns 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Construct the URL for the Reddit API endpoint."""
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    """Check if the request was successful."""
    if response.status_code != 200:
        return (0)
    response = response.json()
    if 'data' in response:
        return (response.get('data').get('subscribers'))

    else:
        return (0)
