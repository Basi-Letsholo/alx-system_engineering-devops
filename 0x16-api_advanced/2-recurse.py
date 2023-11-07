#!/usr/bin/python3
"""Recursively gets list of hot articles in subreddit"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyRedditApi/Sunflower'}

    if hot_list is None:
        hot_list = []

    if after:
        url += f'?after={after}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']

        if after:
            return recurse(subreddit, hot_list, after)

        else:
            return hot_list

    else:
        return None
