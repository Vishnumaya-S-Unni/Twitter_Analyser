import tweepy from textblob import TextBlob
#from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
#from tweepy import Stream


"""class myStreamListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)"""

class twitterapi(api):
    
    def __init__(self):
        # Variables that contain the user credentials to access Twitter API
        ACCESS_TOKEN = "3090484890-r18XN5hnCbRs0YAHMljePwx65rMYcASjPryz5ks"

        ACCESS_TOKEN_SECRET = "74Ygeq732aN7YhKAIojNrxCCFqjjfeduhkJAtKBb7mk7b"

        CONSUMER_KEY = "BTUvvtnyeJXq5j4sWiF29LdW1"

        CONSUMER_SECRET = "yaH1k2bGmNMD17PLmolr1krQURBFCNDDN3bDhZoPqVz5ZdlWks
        self.auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        self.api = tweepy.API(self.auth) 
    def search_twitter(self, track):
        publictweets = api.search(track)
    def sentimental_analyser(self,tweets)
     for tweets in public_tweets:
        print(tweet.text)
        analysis= TextBlob(tweets.text)
        print(analysis.sentiment)
        if analysis.sentiment[0]>0:
            print("POSITIVE")
        elif analysis.sentiment[0]<0:
            print("NEGATIVE")
        else :
            print("NEUTRAL")     
    
if __name__ == "__main__":
    tweets = twitterapi()
    user_input = input("Please enter the items you need to search for (please enter each items with a space between them, for example: hen cheque potato): ")
    items = user_input.split()
    tweets.search_twitter(items)
   # listener = myStreamListener()
   # auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
   # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET

   # stream = Stream(auth, listener)

   # stream.filter(track=['ExcelMEC', 'Narendra Modi','Fifa'])
