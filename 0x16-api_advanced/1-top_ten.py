#!/usr/bin/python3
"""
This script queries the Reddit API and prints
the titles of the first 10 hot posts
for a given subreddit. If the subreddit
is not valid, it prints 'None'.
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints
    the titles of the first 10 hot
    posts for the given subreddit.

    Args:
        subreddit (str): The name of
               the subreddit to search.
    """
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    headers = {'User-Agent': 'CustomClient/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        """
        Check if the request was successful. 
        If not, print 'None' and return.
        """
        if response.status_code != 200:
            print("None")
            return

        """
        Extract the titles of the first 10 
        hot posts and print them.
        """
        data = response.json().get("data", {}).get("children", [])
        for post in data[:10]:
            print(post["data"]["title"])

    except requests.exceptions.RequestException as e:
        print("None")
