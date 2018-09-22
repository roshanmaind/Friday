import pickle
from sys import argv

if len(argv) == 1:
	print("python logout.py <full/path/to/session/pickle>.pkl")
	exit()

with open(argv[1], "wb") as file:
	user = {"logged_in": False, "first_name": "", "last_name": "", "username": "", "access_key": "", "access_secret": ""}
	pickle.dump(user, file)
