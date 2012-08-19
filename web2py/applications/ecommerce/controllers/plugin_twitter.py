# coding: utf-8

from plugin_twitter import get_tweets

def index():
    key = request.vars.key
    tweets = get_tweets(key)
    return dict(tweets=tweets)