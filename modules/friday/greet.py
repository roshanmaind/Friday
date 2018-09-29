from kivy.lang.builder import Builder
Builder.unload_file('modules/friday/login.kv')
Builder.unload_file('modules/twitter_interface/permission.kv')
Builder.unload_file('modules/twitter_interface/login.kv')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import FadeTransition
import time
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)
Config.set('kivy','window_icon','data/friday/res/icon.ico')
from kivy.core.window import Window
Window.__init__()

userG = None

class Empty(Screen):
	def __init__(self, **kwargs):
		super(Screen,self).__init__(**kwargs)	

class Message(Screen):
	text = StringProperty("")
	def __init__(self, **kwargs):
		super(Screen,self).__init__(**kwargs)	
		self.text = "Hello, " + userG["first_name"]

class Manager(ScreenManager):
	empty = ObjectProperty(None)
	message = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(ScreenManager, self).__init__(**kwargs, transition=FadeTransition())
		Clock.schedule_once(self.change, 0.5)

	def change(self, dt):
		self.current = "Message"
		Clock.schedule_once(self.change_back, 1.5)

	def change_back(self, dt):
		self.current = "Empty"
		Clock.schedule_once(self.end, 0.5)

	def end(self, dt):
		App.get_running_app().stop()


class GreetApp(App):
	def build(self):
		self.icon = 'data/friday/res/icon.ico'
		return Manager()

def greet(user):
	global userG
	userG = user
	GreetApp().run()
	#Window.close()

if __name__ == "__main__":
	greet({"first_name": "Roshan"})