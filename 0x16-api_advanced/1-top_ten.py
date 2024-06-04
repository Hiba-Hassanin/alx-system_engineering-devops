#!/usr/bin/python3
import requests

def top_ten(subreddit):
    # Define the base URL for Reddit API
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # Send a GET request to the subreddit
        response = requests.get(base_url, headers=headers, allow_redirects=False)

        # Check if the status code indicates a valid response
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            # Print the titles of the first 10 posts
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
