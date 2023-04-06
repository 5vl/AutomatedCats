from pipedream.script_helpers import (steps, export)

import os
import requests
import tweepy
import re

def upload_media():
    tweepy_auth = tweepy.OAuth1UserHandler(
        "API_KEY",
        "APY_SECRET",
        "CONSUMER_KEY",
        "CONSUMER_SECRET",
    )
    
    tweepy_api = tweepy.API(tweepy_auth)
    url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg,png&api_key=API_KEY"
    cats = requests.request("GET", url).json()
    cat_pic = cats[0]["url"]
    img_data = requests.get(cat_pic).content
    with open("/tmp/catpic.jpg", "wb") as handler:
        handler.write(img_data)
    post = tweepy_api.simple_upload("/tmp/catpic.jpg")
    text = str(post)
    media_id = re.search("media_id=(.+?),", text).group(1)
    payload = {"media": {"media_ids": ["{}".format(media_id)]}, "text": "Here's a new cat! #cats #CatsOfTwitter"}
    os.remove("/tmp/catpic.jpg")
    return payload


def post_tweet(payload):
    return requests.request(
        "POST",
        "https://api.twitter.com/2/tweets",
        json=payload,
        headers={
            "Authorization": "Bearer {}".format(steps["get_access_token"]["$return_value"]),
            "Content-Type": "application/json",
        },
    )

post_tweet(upload_media())
