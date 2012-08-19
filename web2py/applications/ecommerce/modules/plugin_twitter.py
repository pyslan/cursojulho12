# coding: utf-8

import urllib
import json

URL = "http://search.twitter.com/search.json?%s"

def get_tweets(key):
    params = dict(q=key, result_type='mixed', count=5)
    response = urllib.urlopen(URL % urllib.urlencode(params))
    tweets = json.loads(response.read())
    return tweets    
