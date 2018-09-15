from modules import friday, twitter, watson
import os
import pickle


root_path = os.path.realpath(__file__)
root_path = root_path[:len(root_path) - 9]


def load_session():
	with open(str(root_path + "data/friday/last_session.pkl"), "rb") as file:
		user = pickle.load(file)
	return user


def end_session(user):
	# clean user information before saving if the user doesn't want to be remembered
	if not user["logged_in"]:
		user["first_name"] = ""
		user["last_name"] = ""
		user["username"] = ""

	with open(str(root_path + "data/friday/last_session.pkl"), "wb") as file:
		pickle.dump(user, file)


def check_login(user):
	if not user["logged_in"]:
		user = friday.loginator.login(user)
		if user["first_name"] == "" and user["last_name"] == "":
			print("Bye!")
			exit()
		print("Signed in as", user["first_name"], user["last_name"])


def main():
	user = load_session()
	check_login(user)
	
	user = twitter.tweets.get_tweets(user)
	user = watson.analyzer.analyze(user)

	friday.main.run(user)

	end_session(user)

if __name__ == "__main__":
	main()