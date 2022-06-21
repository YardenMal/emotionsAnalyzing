#test 1
# import all the relevant classes
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout


# import pandas as pd

# class ConnectPage(GridLayout):
#     # runs on initialization
#     def __init__(self, **kwargs):
#         # we want to run __init__ of both ConnectPage AAAAND GridLayout
#         super().__init__(**kwargs)
#         self.cols = 2  # used for our grid
#
#
#
#         # widgets added in order, so mind the order.
#         self.add_widget(Label(text='Email*:'))  # widget #1, top left
#         self.Email = TextInput(multiline=False)  # defining self.ip...
#         self.add_widget(self.Email) # widget #2, top right
#
#         self.add_widget(Label(text='Password*:'))
#         self.Password = TextInput(multiline=False)
#         self.add_widget(self.Password)


class LoginPage(MDApp):
    def build(self):
        self.window = GridLayout()
        screen = Screen()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.7}
        self.welcome = MDLabel(text="Welcome to", halign="center",
                               theme_text_color="Custom",
                               text_color=(0, 0, 0, 1),
                               font_style='H4')
        # self.welcome = Label(
        #     text="Welcome to",
        #     font_size = 18)
        self.window.add_widget(self.welcome)
        self.window.add_widget(Image(source="whitelogo.png"))
        self.email = MDLabel(text="Email*", halign="left",
                             theme_text_color="Custom",
                             text_color=(0, 0, 0, 1),
                             font_style='H6')
        self.email = TextInput(multiline=True)
        self.window.add_widget(self.email)
        return self.window


if __name__ == "__main__":
    LoginPage().run()

MDLabel:
text: "SIGN-UP"
font_style: "Button"
font_size: 40
halign: "center"
size_hint_y: None
height: self.texture_size[1]
padding_y: 30
MDTextFieldRound:
hint_text: "Email*"
size_hint_x: None
icon_right: "account"
width: 270
font_size: 20
pos_hint: {"center_x": .5}
normal_color: [0, 0.2, 1, 0.3]
color_active: [1, 1, 1, 1]
MDTextFieldRound:
hint_text: "user-name*"
size_hint_x: None
icon_right: "account"
width: 270
font_size: 20
pos_hint: {"center_x": .5}
normal_color: [0, 0.2, 1, 0.3]
color_active: [1, 1, 1, 1]
MDTextFieldRound:
hint_text: "Age*"
size_hint_x: None
icon_right: "phone"
width: 270
font_size: 20
pos_hint: {"center_x": .5}
normal_color: [0, 0.2, 1, 0.3]
color_active: [1, 1, 1, 1]
MDTextFieldRound:
hint_text: "password*"
password: True
size_hint_x: None
icon_right: "eye-off"
width: 270
font_size: 20
pos_hint: {"center_x": .5}
normal_color: [0, 0.2, 1, 0.3]
color_active: [1, 1, 1, 1]
MDTextFieldRound:
hint_text: "confirm-password*"
size_hint_x: None
password: True
icon_right: "eye-off"
width: 270
font_size: 20
pos_hint: {"center_x": .5}
normal_color: [0, 0.2, 1, 0.3]
color_active: [1, 1, 1, 1]

MDRoundFlatButton:
text: "SIGN-UP"
font_size: 20
pos_hint: {"center_x": .5}
theme_text_color: "Custom"
text_color: [0, 0, 0, 1]