import os
import tweepy
from collections import namedtuple

TwitterConfig = namedtuple('TwitterConfig', [
    'consumer_key',
    'consumer_secret',
    'access_token',
    'access_token_secret'])



def config_factory():

    result = TwitterConfig(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        access_token=os.environ['TOKEN'],
        access_token_secret=os.environ['TOKEN_SECRET'])
    return result


def auth_factory(config: TwitterConfig):
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)

    return auth


AUTH = auth_factory(config_factory())

