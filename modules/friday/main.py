def run(user):
	from kivy.app import App

	try:
		App.get_running_app().stop()
	except:
		pass

	from kivy.config import Config

	Config.set('graphics', 'width', '500')
	Config.set('graphics', 'height', '640')
	Config.set('graphics', 'resizable', False)

	from kivy.uix.screenmanager import Screen
	from kivy.core.window import Window

	