# Dependencies
import pandas as pd
import tweepy
import time
import json
import random

# Extract API key from external json file
keyPairs = open('../../keys/appkey.json')
keyPairs_json = json.load(keyPairs)
consumer_key = keyPairs_json['twtconkey']
consumer_secret = keyPairs_json['twtconsec']
access_token = keyPairs_json['twtacctok']
access_token_secret = keyPairs_json['twtaccsec']

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Quotes to Tweet
happy_quotes = [
    "1. For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "2. Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "3. Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "4. Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "5. Happiness is a warm puppy. - Charles M. Schulz",
    "6. The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "7. Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]

# Create function for tweeting
def tweetMsg(twt):

    api.update_status(twt)

# Twitter credentials

# Tweet a random quote
for twt in happy_quotes:
    print(twt)
    tweetMsg(twt)

# Print success message

# Set timer to run every minute
    time.sleep(5)
