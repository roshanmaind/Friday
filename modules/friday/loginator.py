from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)
Config.set('kivy','window_icon','data/friday/res/icon.ico')
#from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty, BooleanProperty
import h5py
import os


root_path = os.path.realpath(__file__)
root_path = root_path[:len(root_path)- 27]


from kivy.core.window import Window

g_user = None
dbg = None


class Manager(ScreenManager):
	pass


class Greet(Screen):
	pass


class Register(Screen):
	first = StringProperty("")
	last = StringProperty("")
	user = StringProperty("")
	passwd = StringProperty("")
	passwd2 = StringProperty("")
	message = StringProperty("")

	def __init__(self, **kwargs):
		super(Register, self).__init__(**kwargs)
		self.database = dbg

	def sign_up_click(self):
		global g_user
		global dbg
		self.database = dbg
		for entry in self.database:
			if entry[2] == self.user:
				self.message = "Username taken. Use something else."
				self.first = ""
				self.last = ""
				self.user = ""
				self.passwd = ""
				self.passwd2 = ""
				return

		if self.passwd != self.passwd2:
			self.message = "Passwords don't match."
			self.first = ""
			self.last = ""
			self.user = ""
			self.passwd = ""
			self.passwd2 = ""
			return

		if self.user == "":
			self.message = "Username can't be empty"
			self.first = ""
			self.last = ""
			self.user = ""
			self.passwd = ""
			self.passwd2 = ""
			return

		if self.first == "":
			self.message = "First name can't be empty"
			self.first = ""
			self.last = ""
			self.user = ""
			self.passwd = ""
			self.passwd2 = ""
			return

		if self.last == "":
			self.message = "Last name can't be empty"
			self.first = ""
			self.last = ""
			self.user = ""
			self.passwd = ""
			self.passwd2 = ""
			return

		if self.passwd == "":
			self.message = "Password can't be empty"
			self.first = ""
			self.last = ""
			self.user = ""
			self.passwd = ""
			self.passwd2 = ""
			return

		self.database.append([str(self.first), str(self.last), str(self.user), str(self.passwd), "0" * 100, ""])
		for i in range(len(self.database)):
			self.database[i] = [attrib.encode("utf8") for attrib in self.database[i]]
		with h5py.File(str(root_path + "data/friday/users.hdf5"), "w") as users_file:
			d = users_file.create_dataset("users", data=self.database)

		liked = [[str(self.user).encode("utf8"), str("0" * 100).encode("utf8"), "".encode("utf8")]]
		with h5py.File(str(root_path + "data/friday/likes.hdf5"), "a") as file:
			file.create_dataset(str(self.user), data=liked)

		disliked = [[str(self.user).encode("utf8"), str("0" * 100).encode("utf8"), "".encode("utf8")]]
		with h5py.File(str(root_path + "data/friday/dislikes.hdf5"), "a") as file:
			file.create_dataset(str(self.user), data=disliked)

		for i in range(len(self.database)):
			self.database[i] = [attrib.decode("utf8") for attrib in self.database[i]]

		dbg = self.database

		self.message = "Account created!"
		self.first = ""
		self.last = ""
		self.user = ""
		self.passwd = ""
		self.passwd2 = ""


class Signin(Screen):
	user = StringProperty("")
	passwd = StringProperty("")
	message = StringProperty("")
	remember = BooleanProperty(True)

	def __init__(self, **kwargs):
		super(Signin, self).__init__(**kwargs)
		self.database = dbg
		self.remember = True

	def sign_in_click(self):
		global g_user
		global dbg
		self.database = dbg
		for entry in self.database:
			if entry[2] == self.user and entry[3] == self.passwd:
				g_user["first_name"] = entry[0]
				g_user["last_name"] = entry[1]
				g_user["username"] = self.user
				g_user["logged_in"] = True if self.remember else False
				g_user["access_key"] = entry[4]
				g_user["access_secret"] = entry[5]
				App.get_running_app().stop()
				return
		self.message = "Incorrect username or password. Try again."
		self.user = ""
		self.passwd = ""


class Login(App):
	def build(self):
		self.icon = 'data/friday/res/icon.ico'
		return Manager()


def login(user):
	global g_user
	g_user = user
	global dbg
	with h5py.File(str(root_path + "data/friday/users.hdf5"), "r") as users_file:
		database = users_file["users"]
		database = list(database)
		for i in range(len(database)):
			database[i] = [attrib.decode("utf8") for attrib in database[i]]
		dbg = database
	Login().run()
	#Window.close()
	return g_user

if __name__ == "__main__":
	login({})
