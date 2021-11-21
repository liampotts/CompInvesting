import os
import tweepy as tw
import pandas as pd

consumer_key= '7Q9SZ66N5xiP7pipsNnF9WoHm'
consumer_secret= 'UdZYKhrOWTkg9TPB8EfNdMvn9viCyRAy3LtRv4vJLQioyH879y'
access_token= '1461128557921378308-HYS7SqP4ACqbEjACXELplOr8g8kFll'
access_token_secret= 'byVHkBsNPGTLnf3kTnnjCOKFDgOnWly5OFLZsRDFssX9h'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#$JOE"
totalFollowersJOE = []

#Get list of how many people were reached each of last 14 days
for x in range(7,22):
    start_date = datetime.datetime(2021, 11, x, 12, 00, 00)
    end_date = datetime.datetime(2021, 11, x+1, 12, 00, 00)

    # Collect tweets for the day
    tweetsJOE = tw.Cursor(api.search,
                q=search_words,
                lang="en",
                since=start_date,
                until=end_date).items()
    tweetsJOE
    #Get total followers reached each day
    followers = 0
    for tweet in tweetsJOE:
        followers = followers + tweet.user.followers_count
    totalFollowersJOE.append(followers)


