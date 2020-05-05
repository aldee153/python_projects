import tweepy

consumer_key = 'XXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXX'

access_token = 'XXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()
print(user.followers_count)

# Print twitter homepaeg timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(300)

# Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Sara (Cowley) Butler':
        follower.follow()
        break
        #print(follower.name)

# Narcisit Bot
search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        #tweet.retweet()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
