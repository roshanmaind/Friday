import pickle
import os

root_path = os.path.realpath(__file__)
root_path = root_path[:len(root_path) - 21]

with open(str(root_path + "data/friday/last_session.pkl"), "wb") as file:
	user = {"logged_in": False, "first_name": "", "last_name": "", "username": "", "twitter_linked": False}
	pickle.dump(user, file)
