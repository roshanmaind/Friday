from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.watson_service import WatsonApiException
import pickle
import json

username = ""
password = ""
try:
	with open("watson.keys", "rb") as file:
		creds = pickle.load(file)
		username, password = creds[0], creds[1]
except FileNotFoundError:
	print("""
Key files not found in the root directory. The app will not work without key files.
Obtain them from the owner of the official Friday repository, @roshanmaind.

Aborting...
		""")
	exit()

watson = ToneAnalyzerV3(
            username=username,
            password=password,
            version="2017-09-26"
         )


'''Analyze the tone of the tweets in the user dictionary.

The tweets received by the main script will be strings in a list.
The funciton joins all the tweets in one string in which each tweet will be enclosed
within opening and closing <p> html tags. Thus, the function calls the watson tone
analyzer api with content_type="text/html" argument.
'''
def analyze(user):
	global watson

	tweets = user["tweets"]
	tweets_24_hours = user["tweets_24_hours"]
	tone_input = ""
	for tweet in tweets:
		tone_input = tone_input + " <p> " + tweet + " </p> "
	try:
		user["tone"] = watson.tone(tone_input, content_type='text/html').get_result()
	except WatsonApiException as we:
		print(we)
	tone_input = ""
	for tweet in tweets_24_hours:
		tone_input = tone_input + " <p> " + tweet + " </p> "
	try:
		user["tone_24_hours"] = watson.tone(tone_input, content_type='text/html').get_result()
	except WatsonApiException as we:
		print(we)
	if "tone" in user.keys():
		print("Got the following tones in the user's tweets:")
		print(json.dumps(user["tone"], indent=2))
	else:
		print("User has no tweets")
	if "tone_24_hours" in user.keys():
		print("Got the following tones in the user's last 24 hours tweets:")
		print(json.dumps(user["tone"], indent=2))
	else:
		print("User has no tweets made in the last 24 hours")
	return user


if __name__ == "__main__":
	user = {
	         "tweets":
	          [
	            "Hey! This is my first tweet!",
	            "Loving Twitter so far! I just know I'm gonna get addicted to this thing in no time...",
	            "GOD, I can't wait for the new season of Silicon Valley"
	          ]
	       }

	user = analyze(user)
