#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    try:
        # Set the user agent to avoid rate limiting
        headers = {'User-Agent': 'my_app/0.0.1'}

        # Send a GET request to the Reddit API
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the number of subscribers from the response
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            # Return 0 for invalid subreddits
            return 0
    except:
        # Return 0 for any other errors
        return 0
