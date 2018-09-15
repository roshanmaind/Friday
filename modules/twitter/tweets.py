
'''Fetches the tweets made by the user and adds them to the current user session

Currently, this is just a dummy function that returns some random "tweets" text 
for further modules to use.
'''
def get_tweets(user):
	user["tweets"] = [
	                    "Hey! This is my first tweet!", 
	                    "Loving Twitter so far! I just know I'm gonna get addicted to this thing in no time...", 
	                    "GOD, I can't wait for the new season of Silicon Valley"
	                  ]
	return user