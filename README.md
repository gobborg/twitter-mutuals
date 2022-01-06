# compare the mutuals of followed and following on twitter
## two ways to compare the mutuals of who follows you on twitter and whom you follow on twitter

You need:
* tweepy python
* twitter developer keys (I set up mine as a standalone app)

Make 3 files in the same directory as your script file: followers.txt, following.txt, and mutuals.txt. These files can be empty. Whatever is in them will be overwritten.

To increase the amount of data pulled per request, you need to use the 'count' argument in the tweepy.Cursor object. Otherwise, you'll get rate-limited before you pull all of your followers or following (friends).
Using only the api.followers object will only give the most recent 20 followers.
The tweepy library calls "following" 'friends.'

For a detailed comparison of all followed, following, and mutuals list, use the detailed comparison method (line 46).
