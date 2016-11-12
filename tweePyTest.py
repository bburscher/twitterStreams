import os
import tweepy
from confluent_kafka import Producer

TWITTER_APP_KEY = 'gw3sjQj6uHqlTBNiZ0QdJx2vm'
TWITTER_APP_SECRET = 'ka1Eflo0qgRKVVDWPFVuT8WWznasMIgCNy5k1MUGR2CkEHssVq'
TWITTER_KEY = "1327195448-Ymp318HWPQTDVj9axc1MDCMLwbmucj4yyl9pS90"
TWITTER_SECRET = "5zsN8NuVQzb8dO87CrPE2OJdtvykvWuyXPJX6VwkAxD0n"
TOPIC_NAME = os.environ.get('TOPICS', 'election')


auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth)


class StreamListener(tweepy.StreamListener):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.p = Producer({'bootstrap.servers': 'localhost'})

    def on_status(self, status):
        #print(status.text)
        self.p.produce(TOPIC_NAME, status.text.encode('utf-8'))
        self.p.flush()

    def on_error(self, status_code):
        if status_code == 420:
            return False


stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["trump", "clinton", "hillary clinton", "donald trump"])

