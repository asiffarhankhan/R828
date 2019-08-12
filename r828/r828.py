#!/usr/bin/env python3
from config import *
import tweepy

count=0
#passing authentication variables into authentication methods to authenticate

auth = tweepy.OAuthHandler(API_key , API_secret)
auth.set_access_token(token , token_secret)

#calling the tweepy authentication method
api = tweepy.API(auth)

def del_retweets():
	try:
		api.verify_credentials()
		print("\n Authentication done...")

	except Exception as e:
		print("!Error encountered!\nDetails:\n\n"+str(e))

	print('done!')

	#Retrieving Retweets from the authentecating user and deleting one by one

	for tweet in tweepy.Cursor(api.user_timeline).items(5000):
		if tweet.text[0:2]=='RT':
			rem=tweet.id
			count+=1
			api.destroy_status(rem)

#Print information regarding the deletion

	api.update_status('Goodbye all my {} retweets'.format(count))

if __name__=='__main__':
	del_retweets()

