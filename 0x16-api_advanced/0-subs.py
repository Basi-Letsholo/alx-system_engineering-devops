#!/usr/bin/python3
"""Returns number of subscribers for a subreddit"""

import requests


def number_of_subscribers(subreddit):
    url = f'https://reddit.com/r/{subreddit}/about.json'

    headers = {'User-Agent': 'MyRedditApp/1.0'}
    subscribers = 0

    data = requests.get(url, headers=headers)

    if data.status_code == 200:
        data_json = data.json()
        subscribers = data_json['data']['subscribers']
        return subscribers

    else:
        return 0
