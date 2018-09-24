import pickle
from sys import argv


with open("data/friday/session.sav", "wb") as file:
	user = {"logged_in": False, "first_name": "", "last_name": "", "username": "", "access_key": "", "access_secret": "",
	        "liked": [], "disliked": []}
	pickle.dump(user, file)
