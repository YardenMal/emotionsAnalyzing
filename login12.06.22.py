from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.picker import MDDatePicker
import re
import datetime
from datetime import date

helpstr = '''
ScreenManager:
    WelcomeScreen:
    EmailScreen:
    UserNameScreen:
    PasswordScreen:
    SignInScreen:
    MainScreen:
<WelcomeScreen>:
    name : 'welcomescreen'
    MDLabel:
        text:'Welcome To'
        font_style: 'H2'
        halign: 'center'
        pos_hint: {'center_y':0.8}
    Image :
        source : "newlogo.png"
        #opacity : .9
        pos_hint: {"center_x": .5, "center_y": .55}
        size_hint : .7,.7
    MDFloatingActionButton:
        id:disabled_button
        icon: 'account-plus'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.35,'center_y':0.25}
        user_font_size : '35sp'
        on_press:
            root.manager.current = 'emailscreen'
            root.manager.transition.direction = 'left'
    MDLabel:
        text:'Sign up'
        font_style: 'H6'
        pos_hint: {'center_x':0.81,'center_y':0.15}
    MDFloatingActionButton:
        id:disabled_button
        icon: 'account-arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.65,'center_y':0.25}
        user_font_size : '35sp'
        on_press:
            root.manager.current = 'signinscreen'
            root.manager.transition.direction = 'left'
    MDLabel:
        text:'Sign in'
        font_style: 'H6'
        pos_hint: {'center_x':1.11,'center_y':0.15}
<EmailScreen>
    name:'emailscreen'
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id:disabled_button
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:30
        pos_hint: {'center_y':0.02}
    MDLabel:
        text:'Email Address'
        font_style: 'H2'
        halign: 'center'
        pos_hint : {'center_y':0.8}
    MDTextField:
        id:email
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint: (0.7,0.1)
        hint_text : 'Email'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.2}
        user_font_size: '35sp'
        on_press: app.checkEmail()
    MDBoxLayout:
        orientation : 'vertical'
        Image :
            source : "whitelogo.png"
            opacity : .05
            pos_hint: {'center_x': .5,'center_y':0.3}
            size_hint : .7,.7
<UserNameScreen>:
    name:'usernamescreen'
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'emailscreen'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id:disabled_button
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'passwordscreen'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:60
        pos_hint: {'center_y':0.02}
    MDLabel:
        text:'User Details'
        font_style: 'H2'
        halign: 'center'
        pos_hint : {'center_y':0.8}
    MDTextField:
        id:username
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint: (0.7,0.1)
        hint_text : 'username'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:dob
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint: (0.7,0.1)
        hint_text : 'Date of Birth'
        helper_text: 'Required in form DD/MM/YYYY'
        helper_text_mode: 'on_focus'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required : True

    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.2}
        user_font_size: '35sp'
        on_press: app.check_username_age()

    MDBoxLayout:
        orientation : 'vertical'
        Image :
            source : "whitelogo.png"
            opacity : .05
            pos_hint: {'center_x': .5,'center_y':0.3}
            size_hint : .7,.7
    MDFloatingActionButton:
        icon:'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size: '45sp'
        on_press: root.manager.current = 'emailscreen'
            root.manager.transition.direction = 'left'

<PasswordScreen>:
    name : 'passwordscreen'
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id:disabled_button
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value:100
        pos_hint: {'center_y':0.02}
    MDLabel:
        text:'Choose Password'
        font_style: 'H2'
        halign: 'center'
        pos_hint : {'center_y':0.8}
    MDTextField:
        id:password1
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint: (0.7,0.1)
        hint_text : 'password'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'eye-off'
        password : True
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:password2
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint: (0.7,0.1)
        hint_text : 'Verify password'
        helper_text: 'Required'
        password : True
        helper_text_mode: 'on_error'
        icon_right: 'eye-off'
        icon_right_color: app.theme_cls.primary_color
        required : True

    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.2}
        user_font_size: '35sp'
        on_press: app.checkPassword()

    MDBoxLayout:
        orientation : 'vertical'
        Image :
            source : "whitelogo.png"
            opacity : .05
            pos_hint: {'center_x': .5,'center_y':0.3}
            size_hint : .7,.7
    MDFloatingActionButton:
        icon:'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size: '45sp'
        on_press: root.manager.current = 'usernamescreen'
            root.manager.transition.direction = 'left'
<SignInscreen>:
    name : 'signinscreen'
    MDFloatingActionButton:
        icon: 'arrow-left'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'welcomescreen'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id:disabled_button
        disabled: True
        icon: 'arrow-right'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        user_font_size : '45sp'
        on_press:
            root.manager.current = 'mainscreen'
            root.manager.transition.direction = 'left'
    MDLabel:
        text:'Sign in'
        font_style: 'H2'
        halign: 'center'
        pos_hint : {'center_y':0.8}
    MDTextField:
        id:email
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint: (0.7,0.1)
        hint_text : 'Email'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:password
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint: (0.7,0.1)
        hint_text : 'Password'
        helper_text: 'Required'
        password : True
        helper_text_mode: 'on_error'
        icon_right: 'eye-off'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.2}
        user_font_size: '35sp'
        on_press: app.checkEmailSignin()
    MDBoxLayout:
        orientation : 'vertical'
        Image :
            source : "whitelogo.png"
            opacity : .05
            pos_hint: {'center_x': .5,'center_y':0.3}
            size_hint : .7,.7
<MainScreen>:
    name : 'mainscreen'
    MDLabel:
        id:profile_name
        text:'main screen'
        font_style : 'H2'
        halign : 'center'
        pos_hint : {'center_y':0.7}

'''


class WelcomeScreen(Screen):
    pass


class EmailScreen(Screen):
    pass


class UserNameScreen(Screen):
    pass


class PasswordScreen(Screen):
    pass


class SignInScreen(Screen):
    pass


class MainScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcomescreen'))
sm.add_widget(EmailScreen(name='emailscreen'))
sm.add_widget(UserNameScreen(name='usernamescreen'))
sm.add_widget(PasswordScreen(name='passwordscreen'))
sm.add_widget(SignInScreen(name='signinscreen'))
sm.add_widget(MainScreen(name='main_screen'))
email_pattern = "^[a-zA-Z0-9-_]+[\._]?[A-Z a-z 0-9]+@[a-zA-Z0-9]+\.[a-z]+[\._]?[a-z]{2,3}$"


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
     (birthDate.month, birthDate.day))
    return age

class NewApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(helpstr)
        return self.strng

    #check if the email address is valid and that the field is full.
    ###### need to add a check for existing mail###
    def checkEmail(self):
        self.email = self.strng.get_screen('emailscreen').ids.email.text
        email_check_false = True
        try:
            int(self.email)
        except:
            email_check_false = False
        if email_check_false or self.email.split() == []:
            cancel_btn_email_dialogue = MDFlatButton(text='Retry', on_release=self.close_email_dialogue)
            self.dialog = MDDialog(title='This field is required', text="Please enter an Email address", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_email_dialogue])
            self.dialog.open()
        elif self.email:
            # if self.email in user:
            #     cancel_btn_email_dialogue = MDFlatButton(text='Retry', on_release=self.close_email_dialogue)
            #     self.dialog = MDDialog(title='Existing Email', text="This email address is already exist",
            #                            size_hint=(0.7, 0.2),
            #                            buttons=[cancel_btn_email_dialogue])
            #     self.dialog.open()
            if not re.match(email_pattern, self.email):
                cancel_btn_email_dialogue = MDFlatButton(text='Retry', on_release=self.close_email_dialogue)
                self.dialog = MDDialog(title='Invalid Email', text="Please enter a valid Email address",
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_email_dialogue])
                self.dialog.open()
            else:
                self.strng.get_screen('emailscreen').ids.disabled_button.disabled = False
        else:
            self.strng.get_screen('emailscreen').ids.disabled_button.disabled = False

    #check that the fields of user name and date of birth are filled
    #if not, it will raise an error window.
    #this function also check that the user age is above 16.
    def check_username(self):
        self.username_text = self.strng.get_screen('usernamescreen').ids.username.text
        self.dateBirth = self.strng.get_screen('usernamescreen').ids.dob.text
        self.date_time_obj = (datetime.datetime.strptime(self.dateBirth, '%d/%m/%Y')).date()
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or (self.username_text.split() == [] or self.dateBirth.split() == []):
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='These fields are required', text="Please fill all the fields", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()

        else:
            if calculateAge(self.date_time_obj) < 16:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='You are not in the right age', text="You must be 16 years old in order to use Sensound",
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                self.strng.get_screen('usernamescreen').ids.disabled_button.disabled = False

    def check_username_age(self):
        self.username_text = self.strng.get_screen('usernamescreen').ids.username.text
        self.dateBirth = self.strng.get_screen('usernamescreen').ids.dob.text
        username_check_false = True
        username_age_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.username_text.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Invalid user name', text="Please enter a valid user name", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            splitDob = self.dateBirth.split("/")
            s = [str(integer) for integer in splitDob]
            a_string = "".join(s)
            # for i in range(len(splitDob)):
            #     if a_string[0] == "0":
            #         new_string = int(a_string[i + 1:])
            # if a_string.isalpha() or not isinstance(new_string, int):
            if not a_string.isalpha() or a_string != "":
                username_age_false = False

            if len(splitDob) != 3 or username_age_false or self.dateBirth.split() == []:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Invalid Date of birth', text="Please enter a valid date in a DD/MM/YYYY format", size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                self.date_time_obj = (datetime.datetime.strptime(self.dateBirth, '%d/%m/%Y')).date()
                if calculateAge(self.date_time_obj) < 16:
                    cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                    self.dialog = MDDialog(title='You are not in the right age', text="You must be 16 years old in order to use Sensound",
                                           size_hint=(0.7, 0.2),
                                           buttons=[cancel_btn_username_dialogue])
                    self.dialog.open()
                else:
                    self.strng.get_screen('usernamescreen').ids.disabled_button.disabled = False

    def checkPassword(self):
        self.password1 = self.strng.get_screen('passwordscreen').ids.password1.text
        self.password2 = self.strng.get_screen('passwordscreen').ids.password2.text
        password_check_false = True
        try:
            int(self.password1)
        except:
            password_check_false = False
        if password_check_false or self.password1.split() == [] or self.password2.split() == []:
            cancel_btn_password_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Enter password', text="Please input a password", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_password_dialogue])
            self.dialog.open()

        else:
            if self.password1 != self.password2:
                cancel_btn_password_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Verification failed', text="Please enter the same password in both fields", size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_password_dialogue])
                self.dialog.open()
            else:
                self.strng.get_screen('passwordscreen').ids.disabled_button.disabled = False

    def checkEmailSignin(self):
        self.email = self.strng.get_screen('signinscreen').ids.email.text
        self.password = self.strng.get_screen('signinscreen').ids.password.text
        email_check_false = True
        try:
            int(self.email)
        except:
            email_check_false = False
        if email_check_false or self.email.split() == [] or self.password.split()== []:
            cancel_btn_email_dialogue = MDFlatButton(text='Retry', on_release=self.close_email_dialogue)
            self.dialog = MDDialog(title='These fields are required', text="Please fill all the fields", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_email_dialogue])
            self.dialog.open()
        # elif self.email:
        #     if self.email not in user:
        #         cancel_btn_email_dialogue = MDFlatButton(text='Retry', on_release=self.close_email_dialogue)
        #         self.dialog = MDDialog(title='Not Existing Email', text="This email address is not exist. Please Sign up",
        #                                size_hint=(0.7, 0.2),
        #                                buttons=[cancel_btn_email_dialogue])
        #         self.dialog.open()
        #     else:
        #         self.strng.get_screen('signinscreen').ids.disabled_button.disabled = False
        else:
            self.strng.get_screen('signinscreen').ids.disabled_button.disabled = False

    def close_email_dialogue(self, obj):
        self.dialog.dismiss()

    def close_username_dialogue(self, obj):
        self.dialog.dismiss()

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date, year=1999, month=1, day=1, )
        date_dialog.open()

    def get_date(self, date):
        self.dob = date
        self.strng.get_screen('dob').ids.date_picker.text = str(self.dob)
        self.strng.get_screen('dob').ids.second_disabled.disabled = False

        # Storing of DATA
        self.store.put('UserInfo', name=self.username_text, dob=str(self.dob))
        self.username_changer()

    def username_changer(self):
        self.strng.get_screen('mainscreen').ids.profile_name.text = f"Welcome {self.store.get('UserInfo')['name']}"

    def on_start(self):
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.username_changer()
                self.strng.get_screen('mainscreen').manager.current = 'mainscreen'

        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'


NewApp().run()