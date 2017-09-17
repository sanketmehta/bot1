# Dependencies
import tweepy
import time
import json
import random
import datetime
import requests as req
import os

# Extract API key from env variables
consumer_key = os.environ['twtconkey']
consumer_secret = os.environ['twtconsec']
access_token = os.environ['twtacctok']
access_token_secret = os.environ['twtaccsec']
owmkey = os.environ['owmkey']

cityCountry = "london,uk"
base_url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Create function for tweeting
def tweetMsg():

    try:
        upd_url = base_url + "&APPID=" + owmkey + "&q=" + cityCountry
        weather_json = req.get(upd_url).json()
        api.update_status("London Weather as of %s: %s F" %
        (datetime.datetime.now().strftime("%I:%M %p"),
        weather_json["main"]["temp"]))
    except Exception as e:
        print("Exception occured: ", e)

# Tweet london weather every 6 hours
while(True):
    tweetMsg()
    time.sleep(21600)
