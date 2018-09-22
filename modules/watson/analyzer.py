from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.watson_service import WatsonApiException

username = ""
password = ""
with open("watson_creds.txt", "r") as file:
	lines = file.read().split("\n")
	username = lines[0].split(" ")[1]
	password = lines[1].split(" ")[1]

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
	tone_input = ""
	for tweet in tweets:
		tone_input = tone_input + " <p> " + tweet + " </p> "
	try:
		user["tone"] = watson.tone(tone_input, content_type='text/html')
	except WatsonApiException as we:
		print(we)
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
