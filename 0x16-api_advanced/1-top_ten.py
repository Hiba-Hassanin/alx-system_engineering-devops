#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys

def top_ten(subreddit):
    """ Prints the top ten post titles
        from a given subreddit or None if the subreddit is invalid. """
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}

    response = requests.get(url, headers=headers, allow_redirects=False, params=parameters)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title', ''))
    else:
        print(None)
