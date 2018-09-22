import twitter
from modules.twitter_interface import get_token
import pickle
import re
import datetime

'''Fetches the tweets made by the user and adds them to the current user session

Using Twitter API to log in to Twitter account and get tweets
'''


CONSUMER_KEY = 'NUQK4wtw1t8KmyaA0WwOXp4PS'
CONSUMER_SECRET = '9TKbHkmAJZ7aUEAAAxKVtOngqkrIXiNS0bMyQsVSiNoqBaqo9r'


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
		# init
		h = 0
		# years converted to days and then hours and then added
		h += ((year - 1) * 365 + ((year - 1) / 4)) * 24
		# months converted to days and then hours and then added
		h += sum(TweetAge.days_in_months[:month - 1]) * 24
		# adding one more day worth of hours if current year is a leap year
		if (not year % 4) and month > 2:
			h += 24
		# days converted to hours and then added
		h += (day - 1) * 24
		# hours added
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

		tweet_hours = TweetAge.hours(year=int(created_at[YEAR]), month=(TweetAge.months.index(created_at[MONTH]) + 1), day=int(created_at[DATE]), hour=int(created_at[TIME][:2]))
		current_hours = TweetAge.hours(year=now.year, month=now.month, day=now.day, hour=now.hour)

		return current_hours - (tweet_hours + 5.5) < 24


def get_tweets(user):
	linked = user["access_key"] != "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"

	if linked:
		atk, ats = user["access_key"], user["access_secret"]
	else:
		
		atk, ats = get_token.get(CONSUMER_KEY, CONSUMER_SECRET)
		if atk == None:
			return None, user

	api = twitter.Api(consumer_key=CONSUMER_KEY,
	                  consumer_secret=CONSUMER_SECRET,
	                  access_token_key=atk,
	                  access_token_secret=ats,
	                  tweet_mode="extended")
	timeline = api.GetUserTimeline()

	tweets = "\n".join([stat.full_text for stat in timeline if TweetAge.was_made_in_last_24_hours(stat)])

	tweets = re.sub("https.//t.co/[\w]+", "", tweets)
	tweets = re.sub("@[\w]+", "", tweets)
	tweets = re.sub("#[\w]+", "", tweets)
	tweets = tweets.split("\n")
	tweets = [tweet.strip() for tweet in tweets]
	while "" in tweets:
		tweets.remove("")

	user["tweets"] = tweets
	user["access_key"] = atk
	user["access_secret"] = ats

	return (not linked), user


if __name__ == "__main__":
	get_tweets({})