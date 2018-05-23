from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey="7nVOC2blV9MxUr45K54OcugUZ"
csecret="aDtZeV7pjt3J6ovEqtu0VcX14MiX3YL0jqZcDLRqgQQLExDLGO"
atoken="823172633650819072-fItp6uQxbvoXeSb68xFCb0npdJw05Ut"
asecret="rtbn0VdNaSPD6UUp7BvPl7reFreEAI730kP4fdHaiMfqt"

class listener(StreamListener):

    def on_data(self, data):
        try: 
            all_data = json.loads(data)
            
            tweet = all_data["text"]

            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, str(confidence*100)+"%")

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()
            
            return True
        except:
            return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["bitcoin"])
