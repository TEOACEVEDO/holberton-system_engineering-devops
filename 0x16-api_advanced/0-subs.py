#!/usr/bin/python3
"""Return the users name"""
import requests


def number_of_subscribers(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    Reddit = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko)\
                 Chrome/105.0.0.0 Safari/537.36'}

    Ids = requests.get(url, headers=Reddit)

    jason = Ids.json()
    if Ids.status_code == 404:
        return 0

    Data = jason.get("data")
    return Data.get("subscribers")
