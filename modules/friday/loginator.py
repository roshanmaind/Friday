from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config


Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

root = Builder.load_string('''
FloatLayout:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "../../data/loginator/res/bg.jpg"
    Label:
        color: 0.65, 0.65, 0.65, 0.6
        font_name: "../../data/loginator/res/Pacifico.ttf"
        text: "Welcome to Friday"
        font_size: "25dp"
        halign: 'center'
        valign: 'middle'
        pos_hint: {"x": 0, "y": 0.3}
    Label:
        color: 0.8, 0.8, 0.8, 1
        font_name: "../../data/loginator/res/Roboto.ttf"
        text: "or"
        font_size: "19dp"
        halign: 'center'
        valign: 'middle'
        pos_hint: {"x": 0, "y": -0.08}
    Button:
        background_normal: "../../data/loginator/res/button.png"
        background_down: "../../data/loginator/res/buttond.png"
        pos_hint: {"right": .75, "top": 0.5}
        size_hint: (.5,.042)
        Label:
            font_name: "../../data/loginator/res/Lobster.otf"
            font_size: "17dp"
            center: self.parent.center
            text: "Register"
    Button:
        background_normal: "../../data/loginator/res/button2.png"
        background_down: "../../data/loginator/res/button2d.png"
        pos_hint: {"right": .657, "top": 0.38}
        size_hint: (.3,.042)
        Label:
            font_name: "../../data/loginator/res/Lobster.otf"
            font_size: "17dp"
            center: self.parent.center
            text: "Sign in"
''')

class Login(App):
    def build(self):
        return root

def login(user):
    Login().run()
    return user


def twitter_link():
    pass

login(5)
