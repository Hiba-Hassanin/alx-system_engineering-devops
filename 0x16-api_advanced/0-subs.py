#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    try:
        # Send a GET request to the Reddit API, with a custom User-Agent and no redirects
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                                headers={'User-Agent': 'My-User-Agent'},
                                allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the number of subscribers from the response
            return response.json()['data']['subscribers']
        else:
            # Return 0 for invalid subreddits
            return 0
    except:
        # Return 0 for any other errors
        return 0
