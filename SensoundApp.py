from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import re
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import pandas as pd

pattern = "^[a-zA-Z0-9-_]+[\._]?[A-Z a-z 0-9]+@[a-zA-Z0-9]+\.[a-z]+[\._]?[a-z]{2,3}$"

# class to call the popup function
class PopupWindow(Widget):
    def btn(self):
        popFun()


# class to build GUI for a popup window
class P(FloatLayout):
    pass

class InvalidMailAddress(FloatLayout):
    pass

class SignUpScreen(MDApp):
    pass


class PasswordMismatch(FloatLayout):
    pass

# function that displays the content
def popFun():
    show = P()
    window = Popup(title="popup", content=show,
                   size_hint=(None, None), size=(300, 300))
    window.open()


def popInvalidEmailAdress():
    show = InvalidMailAddress()
    window = Popup(title="Error", content=show,
                   size_hint=(None, None), size=(300, 300))
    window.open()


def invalidEmail(email):
    if re.match(pattern, email):
        pass
    else:
        popInvalidEmailAdress()


def popPasswordMismatch():
    show = PasswordMismatch()
    window = Popup(title="Error", content=show,
                   size_hint=(None, None), size=(300, 300))
    window.open()


def checkPasswordMismatch(password1, password2):
    if password1 != password2:
        popPasswordMismatch()


class EmptyFields:
    pass


def popEmptyFields():
    show = EmptyFields()
    window = Popup(title="Error", content=show,
                   size_hint=(None, None), size=(300, 300))
    window.open()


class Sensound(MDApp):
    def Build(self):
        return

    def get_data(self):
        email = self.dialog.content_cls.ids.email.text
        userName = self.dialog.content_cls.ids.userName.text
        age = self.dialog.content_cls.ids.Age.text
        password = self.dialog.content_cls.ids.password.text
        return [email, userName, age, password]



class signupWindow(Screen):
    def get_data(self):
        email, userName, age, password = Sensound.get_data(self)
        return [email, userName, age, password]


    def checkEmpty(self):
        if not (self.email and self.userName and self.email and self.age and self.password):
            popEmptyFields()

    def signupbtn(self):


        # creating a DataFrame of the info
        user = pd.DataFrame([[self.userName, self.email, self.age, self.password]],
                            columns=['Name', 'Email', 'Age', 'Password'])
        if self.email.text != "":
            if self.email.text not in user['Email'].unique():
                # if email does not exist already then append to the csv file
                # change current screen to log in the user now
                # user.to_csv('login.csv', mode='a', header=False, index=False)
                # sm.current = 'login'
                self.userName.text = ""
                self.email.text = ""
                self.password.text = ""
        else:
            # if values are empty or invalid show pop up
            popInvalidEmailAdress()





Sensound().run()