import os
import json

from classTweet import *

def getArchive():
    dir = os.path.dirname(__file__)
    rel_path = "data/tweet.json"
    path = os.path.join(dir, rel_path)

    with open(path,'r') as file:
        run = file.read()
        tweets = json.loads(run[25:])

        archive = {}
        object_id = 0

        for tweet in tweets[:]:

            t = tweet['tweet']

            #BASIC INFO
            id = (t['id_str'])
            text = t['full_text']
            time = t['created_at']
            favs = int(t['favorite_count'])
            retweets = t['retweet_count']

            #CONNECTION
            mentions = t['entities']['user_mentions']

            #MEDIA INFO
            if 'media' in t['entities'].keys():
                media = t['entities']['media'][0]['media_url']
                media_type = t['entities']['media'][0]['type']

            mention_list = []
            if len(t['entities']['user_mentions']) > 0:
                for i in t['entities']['user_mentions']:
                    mention_list.append((i['id_str'],i['name'],i['screen_name']))

            archive[object_id] = Tweet(id,text,time,favs,mention_list)

            object_id += 1

    return archive
