from kivy.app import App
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class Permission(App):
	def allow(self, *largs):
		App.get_running_app().stop()
		
	def deny(self, *largs):
		exit()

	def build(self):
		return FloatLayout()

def consent():
	Config.set('graphics', 'width', '500')
	Config.set('graphics', 'height', '640')
	Config.set('graphics', 'resizable', False)
	Window.__init__()
	Permission().run()
	Window.close()
	return True


if __name__ == "__main__":
	if consent():
		print("allowed")