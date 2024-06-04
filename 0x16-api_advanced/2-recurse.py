#!/usr/bin/python3
""" Recursive function that queries the Reddit API for hot articles """
import requests

def recurse(subreddit, hot_list=[], after=None):
    """ Returns a list of titles of all hot posts in a subreddit """
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, allow_redirects=False, params=parameters)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        for child in children:
            hot_list.append(child.get('data', {}).get('title', ''))

        after = data.get('after', None)
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
