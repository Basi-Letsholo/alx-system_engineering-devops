#!/usr/bin/python3
"""Finds top 10 posts"""

import requests


def top_ten(subreddit):
    limit = 10
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}'
    headers = {'User-Agent': 'MyRedditApi/Sunflower'}

    data = requests.get(url, headers=headers)

    if data.status_code == 200:
        data_j = data.json()

        posts = data_j['data']['children']

        top_posts = []
        for post in posts:
            post_data = post['data']
            top_posts.append(post_data['title'])

        len_list = len(top_posts)

        if len_list == 0:
            print(None)
            return None

        for i in range(0, 10):
            print(top_posts[i])

    else:
        return None
