import os
import tweepy as tw
import pandas as pd
import preprocessor.api as p
from preprocessor.api import clean, tokenize, parse

consumer_key = 'AAAAAAAAAAAAAAAAAAAAAAAA'
consumer_secret = 'BBBBBBBBBBBBBBBBBBBBBBBBB'

access_token = 'CCCCCCCCCCCCCCCCCCCCCCCC'
access_token_secret = 'DDDDDDDDDDDDDDDDDDDDDDD'

# perform authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create our twitter api to access tweets from it
api = tw.API(auth)

search_words = "Korea"
date_since = "2019-11-16"

# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(p.clean(tweet.text))
