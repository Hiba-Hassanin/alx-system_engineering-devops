#!/usr/bin/python3
""" Recursive function that queries the Reddit API and counts keyword occurrences """
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """ Prints the count of given keywords in the titles of hot articles from a subreddit """
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, allow_redirects=False, params=parameters)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        for word in word_list:
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + title.split().count(word)

    after = data.get('after', None)
    if after is not None:
        return count_words(subreddit, word_list, word_count, after)

    sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
    for word, count in sorted_word_count:
        if count > 0:
            print(f"{word}: {count}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
