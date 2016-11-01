'''
Let's make a Twitter bot!
(@peoplefreaking)

This was a fun exercise in using the Twitter API + fiddling with strings in Python.

This will fetch roughly a day's worth of BuzzFeed headlines from their Twitter, 
look for instances of tweetable 'People ___ ___ ___' phrases, and then tweet them out.

After the tweets are downloaded and converted to a single text string, 
the peopleFinder function iterates over the string and settles on the last incidence of a tweetable 'People' phrase, 
before counting spaces in order to nab the following three words as well.

tweetTruncate will then remove that incidence of a 'people phrase' along with the rest of the string past that.
Running peopleFinder again will then return the next-to-last incidence of a tweetable phrase, and so on.
A while loop is used to repeat this operation until the entire string's tweetable phrases have been extracted and tweeted.

'''
import tweepy
import time

CONSUMER_KEY = '##########################################'
CONSUMER_SECRET = '##########################################'
ACCESS_TOKEN = '##########################################'
ACCESS_SECRET = '##########################################'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# obtain tweets
mostrecenttweet = api.user_timeline('buzzfeed', count = 42)
# for tweet in mostrecenttweet:
#     print(tweet.text)

import string

def peopleFinder(tweet_string):
    the_spaces = 0
    substr = ''
    i1 = 0
    i2 = 0
    final_tweet = ''
    for index in range(len(tweet_string)):
        if tweet_string[index:index+6] == 'People':
            i1 = index
    substr = tweet_string[i1:(len(tweet_string))]
    for index in range(len(substr)):
        if substr[index] == ' ':
            the_spaces = the_spaces + 1
            i2 = index
            if the_spaces == 4 :
                break
            else:
                continue
    final_tweet = substr[0:i2]
    final_tweet = string.capwords(final_tweet)
    return(final_tweet)
    
def tweetTruncate(tweet_string):
    substr = ''
    i1 = 0
    i2 = 0
    final_tweet = ''
    for index in range(len(tweet_string)):
        if tweet_string[index:index+6] == 'People':
            i1 = index
    tweet_string = tweet_string[0:i1]
    return(tweet_string)
    
# convert all tweets to a single string
tweetstr = ''
for tweet in mostrecenttweet:
    tweetstr = tweetstr + ' ' + tweet.text    
    
# actual finding + tweeting process
while peopleFinder(tweetstr)[0:6] == 'People':
    final_tweet = peopleFinder(tweetstr)
    api.update_status(final_tweet)
    print(peopleFinder(tweetstr))
    tweetstr = tweetTruncate(tweetstr)
    
    
    
    
