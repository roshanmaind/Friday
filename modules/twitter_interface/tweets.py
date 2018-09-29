import twitter
import pickle
import re
import datetime

'''Fetches the tweets made by the user and adds them to the current user session

Using Twitter API with user access keys got from OAuth to get last 24 hours' tweets.
'''

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

try:
	with open("twitter.keys", "rb") as file:
		creds = pickle.load(file)
		CONSUMER_KEY, CONSUMER_SECRET = creds[0], creds[1]
except FileNotFoundError:
	print("""
Key files not found in the root directory. The app will not work without key files.
Obtain them from the owner of the official Friday repository, @roshanmaind.

Aborting...
		""")
	exit()



class TweetAge():
	months = [
	          "Jan", "Feb", "Mar", "Apr", 
	          "May", "Jun", "Jul", "Aug", 
	          "Sep", "Oct", "Nov", "Dec"
	          ]

	days_in_months = [ 
	                  31, 28, 31, 30, 
	                  31, 30, 31, 31,
	                  30, 31, 30, 31
	                  ]


	@staticmethod
	def hours(year, month, day, hour):
		h = 0
		h += ((year - 1) * 365 + ((year - 1) / 4)) * 24
		h += sum(TweetAge.days_in_months[:month - 1]) * 24
		if (not year % 4) and month > 2:
			h += 24
		h += (day - 1) * 24
		h += hour

		return h


	@staticmethod
	def was_made_in_last_24_hours(stat):
		now = datetime.datetime.now()
		created_at = stat.created_at.split(" ")

		DAY = 0
		MONTH = 1
		DATE = 2
		TIME = 3
		TIMEZONE = 4
		YEAR = 5

		tweet_hours = TweetAge.hours(year=int(created_at[YEAR]), 
		                             month=(TweetAge.months.index(created_at[MONTH]) + 1), 
		                             day=int(created_at[DATE]), 
		                             hour=int(created_at[TIME][:2]))

		current_hours = TweetAge.hours(year=now.year, month=now.month, day=now.day, hour=now.hour)

		return current_hours - (tweet_hours + 5.5) < 24


def get_tweets(user):
	linked = user["access_key"] != "0" * 100

	if linked:
		atk, ats = user["access_key"], user["access_secret"]
	else:
		from modules.twitter_interface import get_token
		atk, ats = get_token.get(CONSUMER_KEY, CONSUMER_SECRET)

	api = twitter.Api(consumer_key=CONSUMER_KEY,
	                  consumer_secret=CONSUMER_SECRET,
	                  access_token_key=atk,
	                  access_token_secret=ats,
	                  tweet_mode="extended")
	timeline = api.GetUserTimeline()

	tweets = "\n".join([stat.full_text for stat in timeline if TweetAge.was_made_in_last_24_hours(stat)])

	tweets = re.sub("https.//t.co/[\w]+", "", tweets)
	tweets = tweets.split("\n")
	tweets = [tweet.strip() for tweet in tweets]
	while "" in tweets:
		tweets.remove("")

	user["tweets"] = tweets
	user["access_key"] = atk
	user["access_secret"] = ats
	if len(user["tweets"]) > 0:
		print("Received the following tweets of the user:-")
		for tweet in user["tweets"]:
			print(tweet)
	return (not linked), user


if __name__ == "__main__":
	get_tweets({})