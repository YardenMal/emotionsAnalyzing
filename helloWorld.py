from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Window.size=(600,670)
class Myapp(MDApp):
    def build(self):
        self.title = "Signup Screen"
        return

    def close_dilog(self, obj):
        self.dialog.dismiss()

    def post(self):
        print(self.root.ids.username.text)
        close = MDRectangleFlatButton(text="Close", on_release=self.close_dilog)
        more = MDRectangleFlatButton(text="Download")
        self.dialog = MDDialog(title=f"POSTING...",
                               size_hint_y=None,
                               height="600",
                               text=f"Author : ",
                               size_hint=(0.9, 1),
                               buttons=[close, more],
                               )
        self.dialog.open()


class windowManager(ScreenManager):
    pass


sm = windowManager()

Myapp().run()
