from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivy.uix.screenmanager import Screen
from kivy.core.window import Window


allowed = False

class Main(Screen):
	pass

class Permission(App):
	def allow(self):
		global allowed
		allowed = True
		Window.close()
		return
		
	def deny(self):
		global allowed
		allowed = False
		Window.close()
		return

	def build(self):
		return Main()

def consent():
	global allowed
	try:
		Permission().run()
	except:
		pass
	return allowed


if __name__ == "__main__":
	print(consent())