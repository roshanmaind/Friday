from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty, BooleanProperty
import h5py
import os


root_path = os.path.realpath(__file__)
root_path = root_path[:len(root_path)- 27]


Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)


g_user = None


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
		with h5py.File(str(root_path + "data/friday/users.hdf5"), "r") as users_file:
			database = users_file["users"]
			database = list(database)
			for i in range(len(database)):
				database[i] = [attrib.decode("utf8") for attrib in database[i]]
			self.database = database

	def sign_up_click(self):
		global g_user

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

		self.database.append([str(self.first), str(self.last), str(self.user), str(self.passwd), "N"])
		for i in range(len(self.database)):
			self.database[i] = [attrib.encode("utf8") for attrib in self.database[i]]
		with h5py.File(str(root_path + "data/friday/users.hdf5"), "w") as users_file:
			d = users_file.create_dataset("users", data=self.database)
		self.message = "Account created! Restart Friday to login."
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
		with h5py.File(str(root_path + "data/friday/users.hdf5"), "r") as users_file:
			database = users_file["users"]
			database = list(database)
			for i in range(len(database)):
				database[i] = [attrib.decode("utf8") for attrib in database[i]]
			self.database = database
		self.remember = True

	def sign_in_click(self):
		global g_user
		for entry in self.database:
			if entry[2] == self.user and entry[3] == self.passwd:
				g_user["first_name"] = entry[0]
				g_user["last_name"] = entry[1]
				g_user["username"] = self.user
				g_user["logged_in"] = True if self.remember else False
				g_user["twitter_linked"] = True if entry[4] == "Y" else False
				App.get_running_app().stop()
				return
		self.message = "Incorrect username or password. Try again."
		self.user = ""
		self.passwd = ""


class Login(App):
	def build(self):
		return Manager()


def login(user):
	global g_user
	g_user = user
	Login().run()
	return g_user