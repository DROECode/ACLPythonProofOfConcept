#! Written in ACL for Audit Script
# This script will expect inputs to the gettweetmain
# Inputs: ACL script passing in:
#       ConsumerKey
#       ConsumerSecret
#       Owner
#       OwnerID
#       AccessToken
#       AccessTokenSecret
# Outputs:
#       s_TwitResponse -
#
#! Python
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListner
import argparse
import json
import string
import time

#def process_or_store(tweet)
    #print(json.dumps(tweet,indent=4)) # pretty print to screen

def gettweetmain(ConsumerKey,ConsumerSecret,Owner,OwnerID,AccessToken,AccessTokenSecret)
    username='<riiiiight-get-your-own>'
    Tauth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
    Tauth.set_access_token(AcecssToken,AccessTokenSecret)
    Tapi = tweepy.API(Tauth)
    for status in tweepy.Cursor(Tapi.home_timeline).items(1)
        # Process a single status from the response
        s_TwitResponse = json.dump(status.json, indent=4)
        return(s_TwitResponse)
