import h5py
import pickle

def split_list(artists, seperator):
	for i in range(len(artists)):
		artists += artists[i].split(seperator)
	for artist in artists:
		if artist.split(seperator) != [artist]:
			artists.remove(artist)


def individualize(artists):
	for seperator in (",", "+", "&", "Featuring"):
		artists = split_list(artists, seperator)
	for i in range(len(artists)):
		artists[i] = artists[i].strip()
	artists = list(set(artists))
	return artists


def caps_alpha_numeric(string):
	string = string.upper()
	string = list(string)
	for i in range(len(string)):
		if (not string[i].isalnum()) or string[i] == " ":
			string[i] = ""
	string = "".join(string)
	return string


def tweets_have(user, string):
	tweets_tone = user["tone"]["sentences_tone"]
	tweets = [sentences["text"] for sentences in tweets_tone]
	for i in range(len(tweets)):
		if string in tweets[i] or caps_alpha_numeric(string) in tweets[i]:
			return True, tweets_tone[i]["tones"]
	return False, None


def recommend(user):
	songs, liked, disliked = None, None, None
	with open("../../data/friday/songs.bin", "rb") as file:
		songs = pickle.load(file)
	with h5py.File("../../data/friday/liked.hdf5", "r") as file:
		liked = file[user["username"]]
	with h5py.File("../../data/friday/disliked.hdf5", "r") as file:
		disliked = file[user["username"]]
	liked = [s.decode("utf8") for s in liked]
	disliked = [s.decode("utf8") for s in disliked]

	all_songs = set()
	all_artists = set()
	liked_artists = {}
	disliked_artists = {}
	liked_genre = {}
	disliked_genre = {}
	final_pool = []

	for genre in songs.keys():
		for song in songs[genre]:
			# giving "greatest of all time" songs a preference
			if genre == "goat":
				all_songs.add(song + [1])
			else:
				all_songs.add(song + [0])

			artists = individualize([song[0].split("~")[1].strip()])
			for artist in artists:
				all_artists.add(artist)

	for song in user["liked"]:
		artists = individualize([song[0].split("~")[1].strip()])
		for artist in artists:
			if artist in liked_artists.keys():
				liked_artists[artist] += 1
			else:
				liked_artists[artist] = 1
		if song[2] in liked_genre.keys():
			liked_genre[song[2]] += 1
		else:
			liked_genre[song[2]] = 1

	for song in user["disliked"]:
		artists = individualize([song[0].split("~")[1].strip()])
		for artist in artists:
			if artist in disliked_artists.keys():
				disliked_artists[artist] += 1
			else:
				disliked_artists[artist] = 1
		if song[2] in disliked_genre.keys():
			disliked_genre[song[2]] += 1
		else:
			disliked_genre[song[2]] = 1


	"""
	Criteria of picking songs
	
	Likelyhood of a song being picked is based upon 4 aspects
	1. User's mentions of songs/artists/genres in tweets along with the sentiment of the tweet
	2. Overall sentiment of user's tweets
	3. User's liked and disliked songs
	4. Randomness
	"""

	for song in all_songs:
		# mentions in tweets
		negatives = ["anger", "sadness"]
		positives = ["joy"]

		artists = individualize([song[0].split("~")[1].strip()])

		## check the mention of this song's genre
		they_do, tones = tweets_have(user, song[2])	
		if they_do:
			tone_ids = [t["tone_id"] for t in tones]
			if any([pos in tone_ids for pos in positives]):
				song[3] += 3
			elif any([neg in tone_ids for neg in negatives]):
				song[3] -= 3
			else:
				song[3] += 2

		## check the mention of this song's artist's name
		for artist in artists:
			they_do, tones = tweets_have(user, artist)
			if they_do:
				tone_ids = [t["tone_id"] for t in tones]
				if any([pos in tone_ids for pos in positives]):
					song[3] += 3
				elif any([neg in tone_ids for neg in negatives]):
					song[3] -= 3
				else:
					song[3] += 2

		## check the mention of this song's name
		they_do, tones = tweets_have(user, song[0].split("~")[0].strip())
		if they_do:
			tone_ids = [t["tone_id"] for t in tones]
			for s in all_songs:
				### judge other songs based on artists
				for artist in artists:
					if artist in s[0]:
						if any([pos in tone_ids for pos in positives]):
							s[3] += 3
						elif any([neg in tone_ids for neg in negatives]):
							s[3] -= 3
						else:
							s[3] += 2
				### judge other songs based on genre
				if s[2] == song[2]:
					if any([pos in tone_ids for pos in positives]):
						s[3] += 3
					elif any([neg in tone_ids for neg in negatives]):
						s[3] -= 3
					else:
						s[3] += 2

		# overall sentiment of the tweets
		link = {
			"anger": ("hip-hop", "rock", "edm"),
			"fear": (),                        ## neutral sentiment in this context
			"joy": ("hip-hop", "rock", "edm", "pop", "country"),
			"sadness": ("classical", "rock", "pop", "jazz", "country"),
			"analytical": ("classical", "jazz", "country"),
			"confident": (),                   ## neutral sentiment in this context
			"tentative": ()                    ## neutral sentiment in this context
		}
		overall_sentiment = user["tone"]["document_tone"]["tones"]

		for sentiment in overall_sentiment:
				if song[2] in link[sentiment["tone_id"]]:
					song[3] += round(sentiment["score"] * 2)

		# likes and dislikes
		## likes
		for artist in artists:
			if artist in liked_artists.keys():
				song[3] += 3 * liked_artists[artist]
		if song[2] in liked_genre.keys():
			song[3] += 1 * liked_genre[song[2]]

		## dislikes
		for artist in artists:
			if artist in disliked_artists.keys():
				song[3] -= 3 * disliked_artists[artist]
		if song[2] in disliked_genre.keys():
			song[3] -= 1 * disliked_genre[song[2]]		

	lowest = min([song[3] for song in all_songs])
	extra = 1 - lowest if lowest < 0 else 0
	for song in all_songs:
		final_pool += [song] * (song[3] + extra)

	if "songs" not in user.keys():
		user["songs"] = []

	for i in range(10):
		idx = random.randint(0, len(final_pool) - 1)
		while final_pool[idx] in user["songs"]:
			idx = random.randint(0, len(final_pool) - 1)
		user["songs"].append(final_pool[idx])
		
	return user