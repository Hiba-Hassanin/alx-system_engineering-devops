#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[]):
    """
    Returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function returns None.
    """
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    children = data.get('children')
    hot_list.extend([child.get('data').get('title') for child in children])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list)
    else:
        return hot_list
