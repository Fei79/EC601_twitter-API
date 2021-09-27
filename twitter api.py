import tweepy

consumer_key = "XXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_latest_tweets_withHashTags():
    for tweet in tweepy.Cursor(api.search_30_day, label='search', query="#Boston").items(10):
        print('Tweet by:@'+tweet.user.screen_name)

def count_tweets_number_withHashTags():
    for page in tweepy.Cursor(api.search_30_day, label='search', query="#Boston").pages(1):
        count = len(page)
        query=["#Boston"]
        print( "Count of tweets in each page for  " + str(query) + " : " +  str(count))

get_latest_tweets_withHashTags()
count_tweets_number_withHashTags()
