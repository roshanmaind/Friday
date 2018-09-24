

userG = {}

def go_to(url):
	driver = webdriver.Firefox()
	driver.get(url)


class Root(Screen):
	uname = StringProperty("")
	uname_size = StringProperty("")
	song1 = StringProperty("")
	song2 = StringProperty("")
	song3 = StringProperty("")
	song4 = StringProperty("")
	song5 = StringProperty("")
	song6 = StringProperty("")
	song7 = StringProperty("")
	song8 = StringProperty("")
	song9 = StringProperty("")
	song10 = StringProperty("")
	song1_like_image = StringProperty("")
	song2_like_image = StringProperty("")
	song3_like_image = StringProperty("")
	song4_like_image = StringProperty("")
	song5_like_image = StringProperty("")
	song6_like_image = StringProperty("")
	song7_like_image = StringProperty("")
	song8_like_image = StringProperty("")
	song9_like_image = StringProperty("")
	song10_like_image = StringProperty("")
	song1_dislike_image = StringProperty("")
	song2_dislike_image = StringProperty("")
	song3_dislike_image = StringProperty("")
	song4_dislike_image = StringProperty("")
	song5_dislike_image = StringProperty("")
	song6_dislike_image = StringProperty("")
	song7_dislike_image = StringProperty("")
	song8_dislike_image = StringProperty("")
	song9_dislike_image = StringProperty("")
	song10_dislike_image = StringProperty("")

	def __init__(self, **kwargs):
		self.uname=userG["username"]
		self.uname_size = str(220 // len(self.uname)) + "dp"
		self.songs = userG["songs"]
		self.song1_like_image, self.song2_like_image, self.song3_like_image, self.song4_like_image, self.song5_like_image = ["../../data/friday/res/like.png"] * 5
		self.song6_like_image, self.song7_like_image, self.song8_like_image, self.song9_like_image, self.song10_like_image = ["../../data/friday/res/like.png"] * 5
		self.song1_dislike_image, self.song2_dislike_image, self.song3_dislike_image, self.song4_dislike_image, self.song5_dislike_image = ["../../data/friday/res/dislike.png"] * 5
		self.song6_dislike_image, self.song7_dislike_image, self.song8_dislike_image, self.song9_dislike_image, self.song10_dislike_image = ["../../data/friday/res/dislike.png"] * 5
		self.song1, self.song2, self.song3, self.song4, self.song5, self.song6, self.song7, self.song8, self.song9, self.song10 = (s[0] for s in self.songs)
		self.liked = [False] * 10
		super(Screen,self).__init__(**kwargs)


	def logout(self):
		userG["logged_in"] = False
		userG["logged_out"] = True
		App.get_running_app().stop()
		return

	def like_song1(self):
		self.song1_like_image = "../../data/friday/res/liked.png"
		self.song1_dislike_image = "../../data/friday/res/dislike.png"
		global userG
		userG["liked"].append(self.songs[0])
		if self.songs[0] in userG["disliked"]:
			userG["disliked"].remove(self.songs[0])

	def dislike_song1(self):
		self.song1_dislike_image = "../../data/friday/res/disliked.png"
		self.song1_like_image = "../../data/friday/res/like.png"
		global userG
		userG["disliked"].append(self.songs[0])
		if self.songs[0] in userG["liked"]:
			userG["liked"].remove(self.songs[0])

	def listen_song1(self):
		go_to(self.songs[0][1])

	def like_song2(self):
		self.song2_like_image = "../../data/friday/res/liked.png"
		self.song2_dislike_image = "../../data/friday/res/dislike.png"
		global userG
		userG["liked"].append(self.songs[1])
		if self.songs[1] in userG["disliked"]:
			userG["disliked"].remove(self.songs[1])

	def dislike_song2(self):
		self.song2_dislike_image = "../../data/friday/res/disliked.png"
		self.song2_like_image = "../../data/friday/res/like.png"
		global userG
		userG["disliked"].append(self.songs[1])
		if self.songs[1] in userG["liked"]:
			userG["liked"].remove(self.songs[1])

	def listen_song2(self):
		go_to(self.songs[1][1])

	def like_song3(self):
		self.song3_like_image = "../../data/friday/res/liked.png"
		self.song3_dislike_image = "../../data/friday/res/dislike.png"
		global userG
		userG["liked"].append(self.songs[2])
		if self.songs[2] in userG["disliked"]:
			userG["disliked"].remove(self.songs[2])

	def dislike_song3(self):
		self.song3_dislike_image = "../../data/friday/res/disliked.png"
		self.song3_like_image = "../../data/friday/res/like.png"
		global userG
		userG["disliked"].append(self.songs[2])
		if self.songs[2] in userG["liked"]:
			userG["liked"].remove(self.songs[2])

	def listen_song3(self):
		go_to(self.songs[2][1])

	def like_song4(self):
		self.song4_like_image = "../../data/friday/res/liked.png"
		self.song4_dislike_image = "../../data/friday/res/dislike.png"
		global userG
		userG["liked"].append(self.songs[3])
		if self.songs[3] in userG["disliked"]:
			userG["disliked"].remove(self.songs[3])

	def dislike_song4(self):
		self.song4_dislike_image = "../../data/friday/res/disliked.png"
		self.song4_like_image = "../../data/friday/res/like.png"
		global userG
		userG["disliked"].append(self.songs[3])
		if self.songs[3] in userG["liked"]:
			userG["liked"].remove(self.songs[3])

	def listen_song4(self):
		go_to(self.songs[3][1])

	def like_song5(self):
		self.song5_like_image = "../../data/friday/res/liked.png"
		self.song5_dislike_image = "../../data/friday/res/dislike.png"
		global userG
		userG["liked"].append(self.songs[4])
		if self.songs[4] in userG["disliked"]:
			userG["disliked"].remove(self.songs[4])

	def dislike_song5(self):
		self.song5_dislike_image = "../../data/friday/res/disliked.png"
		self.song5_like_image = "../../data/friday/res/like.png"
		global userG
		userG["disliked"].append(self.songs[4])
		if self.songs[4] in userG["liked"]:
			userG["liked"].remove(self.songs[4])

	def listen_song5(self):
		go_to(self.songs[4][1])

	def like_song6(self):
		self.song6_like_image = "../../data/friday/res/liked.png"
		self.song6_dislike_image = "../../data/friday/res/dislike.png"
		global userG
		userG["liked"].append(self.songs[5])
		if self.songs[5] in userG["disliked"]:
			userG["disliked"].remove(self.songs[5])

	def dislike_song6(self):
		self.song6_dislike_image = "../../data/friday/res/disliked.png"
		self.song6_like_image = "../../data/friday/res/like.png"
		global userG
		userG["disliked"].append(self.songs[5])
		if self.songs[5] in userG["liked"]:
			userG["liked"].remove(self.songs[5])

	def listen_song6(self):
		go_to(self.songs[5][1])

	def like_song7(self):
		self.song7_like_image = "../../data/friday/res/liked.png"
		self.song7_dislike_image = "../../data/friday/res/dislike.png"
		global userG
		userG["liked"].append(self.songs[6])
		if self.songs[6] in userG["disliked"]:
			userG["disliked"].remove(self.songs[6])

	def dislike_song7(self):
		self.song7_dislike_image = "../../data/friday/res/disliked.png"
		self.song7_like_image = "../../data/friday/res/like.png"
		global userG
		userG["disliked"].append(self.songs[6])
		if self.songs[6] in userG["liked"]:
			userG["liked"].remove(self.songs[6])

	def listen_song7(self):
		go_to(self.songs[6][1])

	def like_song8(self):
		self.song8_like_image = "../../data/friday/res/liked.png"
		self.song8_dislike_image = "../../data/friday/res/dislike.png"
		global userG
		userG["liked"].append(self.songs[7])
		if self.songs[7] in userG["disliked"]:
			userG["disliked"].remove(self.songs[7])

	def dislike_song8(self):
		self.song8_dislike_image = "../../data/friday/res/disliked.png"
		self.song8_like_image = "../../data/friday/res/like.png"
		global userG
		userG["disliked"].append(self.songs[7])
		if self.songs[7] in userG["liked"]:
			userG["liked"].remove(self.songs[7])

	def listen_song8(self):
		go_to(self.songs[7][1])

	def like_song9(self):
		self.song9_like_image = "../../data/friday/res/liked.png"
		self.song9_dislike_image = "../../data/friday/res/dislike.png"
		global userG
		userG["liked"].append(self.songs[8])
		if self.songs[8] in userG["disliked"]:
			userG["disliked"].remove(self.songs[8])

	def dislike_song9(self):
		self.song9_dislike_image = "../../data/friday/res/disliked.png"
		self.song9_like_image = "../../data/friday/res/like.png"
		global userG
		userG["disliked"].append(self.songs[8])
		if self.songs[8] in userG["liked"]:
			userG["liked"].remove(self.songs[8])

	def listen_song9(self):
		go_to(self.songs[8][1])

	def like_song10(self):
		self.song10_like_image = "../../data/friday/res/liked.png"
		self.song10_dislike_image = "../../data/friday/res/dislike.png"
		global userG
		userG["liked"].append(self.songs[9])
		if self.songs[9] in userG["disliked"]:
			userG["disliked"].remove(self.songs[9])

	def dislike_song10(self):
		self.song10_dislike_image = "../../data/friday/res/disliked.png"
		self.song10_like_image = "../../data/friday/res/like.png"
		global userG
		userG["disliked"].append(self.songs[9])
		if self.songs[9] in userG["liked"]:
			userG["liked"].remove(self.songs[9])

	def listen_song10(self):
		go_to(self.songs[9][1])


class Friday(App):
	def build(self):
		return Root()

def run(user):
	from kivy.app import App
	try:
		App.get_running_app().stop()
	except:
		pass

	from kivy.config import Config
	Config.set('graphics', 'width', '1120')
	Config.set('graphics', 'height', '700')
	Config.set('graphics', 'resizable', False)

	from kivy.uix.screenmanager import Screen, ScreenManager
	from kivy.properties import StringProperty
	from selenium import webdriver
	
	global userG
	userG = user
	userG["logged_out"] = False
	Friday().run()
	user = userG
	return user

if __name__ == "__main__":
	run({"username": "roshanmaind",
	     "songs": [["Song Name - Artist Name", "https://www.youtube.com", "genre"],
		             ["Song Name - Artist Name", "https://www.youtube.com", "genre"],
		             ["Song Name - Artist Name", "https://www.youtube.com", "genre"],
		             ["Song Name - Artist Name", "https://www.youtube.com", "genre"],
		             ["Song Name - Artist Name", "https://www.youtube.com", "genre"],
		             ["Song Name - Artist Name", "https://www.youtube.com", "genre"],
		             ["Song Name - Artist Name", "https://www.youtube.com", "genre"],
		             ["Song Name - Artist Name", "https://www.youtube.com", "genre"],
		             ["Song Name - Artist Name", "https://www.youtube.com", "genre"],
		             ["Song Name - Artist Name", "https://www.youtube.com", "genre"]
		             ],
	     "liked": [],
	     "disliked": []
	     })
