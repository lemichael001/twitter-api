import tweepy

api_key = 'YOUR KEY HERE'
api_secret_key = 'YOUR KEY HERE'
access_token = 'YOUR TOKEN HERE'
access_token_secret = 'YOUR TOKEN HERE'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#First attempt at gather user tweets

twitter_name = input("Enter your Twitter Handle: ")
for name in twitter_name:
    try:
        tweet = api.user_timeline(screen_name = twitter_name, count = 10)
    except tweepy.TweepError as e:
            twitter_name = input("The handle you entered is invalid, please try again: ")
print(tweet)
