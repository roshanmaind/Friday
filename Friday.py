# Python 3.6.5

from modules import friday, twitter
from os import system
import pickle


if __name__ == "__main__":
    with open("data/friday/last_session.pkl", "rb") as file:
        user = pickle.load(file)
    if not user["logged_in"]:
        user = friday.loginator.login(user)
        user["logged_in"] = True
    if not user["twitter_linked"]:
        user = twitter.linker.link(user)
        user["twitter_linked"] = True
