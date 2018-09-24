from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from pygame import error

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

class Permission(App):
	def allow(self, *largs):
		super(Permission, self).stop(*largs)
		App.get
		self.stop()
		
	def deny(self, *largs):
		super(Permission, self).stop(*largs)
		exit()

	def build(self):
		return FloatLayout()

def consent():
	Permission().run()
	from kivy.core.window import Window
	Window.close()
	return True


if __name__ == "__main__":
	if consent():
		print("allowed")