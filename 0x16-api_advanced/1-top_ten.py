#!/usr/bin/python3
"""
This script queries the Reddit API and
prints the titles of the first 10
hot posts for a given subreddit.
If the subreddit is not valid,
it prints 'None'.
"""
import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and
    prints the titles of the
    first 10 hot posts.

    Args:
        subreddit (str):
        The name of the subreddit
        to search
    """
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    """
        Check if the request was
        successful. If not,
        print 'None' and
        return.
    """
    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
