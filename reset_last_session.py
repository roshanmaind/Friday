import pickle

with open("data/friday/last_session.pkl", "wb") as file:
    user = {"logged_in": False, "first_name": "first", "last_name": "last", "username": "username", "twitter_linked": False}
    pickle.dump(user, file)
