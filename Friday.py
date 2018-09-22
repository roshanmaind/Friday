from modules.twitter_interface import tweets
from modules import friday, watson
import os
import pickle
import h5py


root_path = os.path.realpath(__file__)
root_path = root_path[:len(root_path) - 9]


def load_session():
	with open(str(root_path + "data/friday/session.pkl"), "rb") as file:
		user = pickle.load(file)
	return user


def end_session(user):
	# clean user information before saving if the user doesn't want to be remembered
	if not user["logged_in"]:
		user["first_name"] = ""
		user["last_name"] = ""
		user["username"] = ""

	with open(str(root_path + "data/friday/session.pkl"), "wb") as file:
		pickle.dump(user, file)


def check_login(user):
	if not user["logged_in"]:
		from modules.friday import loginator
		user = loginator.login(user)
		if user["first_name"] == "" and user["last_name"] == "":
			print("Bye!")
			exit()
		print("Signed in as", user["first_name"], user["last_name"])

def save_user_keys(user):
	database = None
	with h5py.File(str(root_path + "data/friday/users.hdf5"), "r") as users_file:
		database = list(users_file["users"])
		for i in range(len(database)):
			if database[i][2] == user["username"].encode("utf8"):
				database[i][4] = user["access_key"].encode("utf8")
				database[i][5] = user["access_secret"].encode("utf8")
				break
	with h5py.File(str(root_path + "data/friday/users.hdf5"), "w") as users_file:
			d = users_file.create_dataset("users", data=database)

def main():
	user = load_session()
	check_login(user)
	
	new_keys, user = tweets.get_tweets(user)

	if new_keys is None:
		exit()
	if new_keys == True:
		print("Saving user access tokens")
		save_user_keys(user)

	user = watson.analyzer.analyze(user)

	friday.main.run(user)

	end_session(user)

if __name__ == "__main__":
	main()