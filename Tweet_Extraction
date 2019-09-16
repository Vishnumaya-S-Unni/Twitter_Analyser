from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contain the user credentials to access Twitter API
ACCESS_TOKEN = "3090484890-r18XN5hnCbRs0YAHMljePwx65rMYcASjPryz5ks"
ACCESS_TOKEN_SECRET = "74Ygeq732aN7YhKAIojNrxCCFqjjfeduhkJAtKBb7mk7b"
CONSUMER_KEY = "BTUvvtnyeJXq5j4sWiF29LdW1"
CONSUMER_SECRET = "yaH1k2bGmNMD17PLmolr1krQURBFCNDDN3bDhZoPqVz5ZdlWks"


class myStreamListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    listener = myStreamListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)

    stream.filter(track=['ExcelMEC', 'Narendra Modi','Fifa'])
