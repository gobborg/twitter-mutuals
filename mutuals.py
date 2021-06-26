'''
compare the mutuals of followed and following on twitter
'''

import tweepy, sys
from difflib import Differ

# Authenticate to Twitter
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
api = tweepy.API(auth)
'''
# To test access to Twitter
try:
    api.verify_credentials()
    print('Authentication OK')
except:
    print('Error during authentication')
'''

#create lists to compare them
followers = ''
following = ''
mutuals = ''

#for the next parts, if you don't do count='' instead of items(amount), you'll get rate-limited

#FOLLOWERS
for follower in tweepy.Cursor(api.followers, count='200').items():
	followers += follower.name + '\n'
open('followers.txt','w').write(followers)
	
#FOLLOWING
for friend in tweepy.Cursor(api.friends, count='200').items():
	following += friend.name + '\n'
open('following.txt','w').write(following)

#MUTUALS (simple list of mutuals)
with open('followers.txt','r') as f, open('following.txt','r') as g:
	fa = f.read().splitlines()
	ga = g.read().splitlines()
	m = [item for item in fa if item in ga]
open('mutuals.txt','w').write("\n".join(m))

'''
#MUTUALS (detailed comparison of all followed, following, and mutuals)
with open('followers.txt','r') as f, open('following.txt','r') as g:
	differ = Differ()
	for line in differ.compare(f.readlines(), g.readlines()):
		mutuals += line
open('mutuals.txt','w').write("\n".join(m))
# - means follows you; you don't follow them
# + means you follow them; they don't follow you
# _ means mutuals
'''
