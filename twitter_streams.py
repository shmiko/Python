#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "29664554-I4tOznq8ztIn3vUzYktE7yAfM7Oq0eCrCmqoymsay"
access_token_secret = "Uti9xGMpdDfM322j5G7EduSRh5QbJ3inh2b75JapGfuZu"
consumer_key = "K8Kggw18Dd3WsqCYfq0vzdeQx"
consumer_secret = "IsdP2TPrtSiRFeZnYuwjzlN1UHBeZFZtRa4Ippswe0VAHxGBr5"

class TweetListener(StreamListener):
    # A listener handles tweets are the received from the stream.
    #This is a basic listener that just prints received tweets to standard output
 
    def on_data(self, data):
        print data
        return True
 
    def on_error(self, status):
        print status
 
#printing all the tweets to the standard output
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
stream = Stream(auth, TweetListener())
stream.filter(track=['python', 'javascript', 'ruby'])