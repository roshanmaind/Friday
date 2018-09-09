from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

class Manager(ScreenManager):
    pass

class Greet(Screen):
    pass

class Register(Screen):
    pass

class Signin(Screen):
    pass

class Login(App):
    def __init__(self, user, **kwargs):
        super(Login, self).__init__(**kwargs)
        self.user = user

    def build(self):
        return Manager()


def login(user):
    Login(user).run()
    return user


login(5)
