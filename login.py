from kivy.core.text import Label
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.storage.jsonstore import JsonStore
import re
import pickle
import datetime
from datetime import date
import mysql.connector
from kivy.app import App
from plyer import filechooser
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
# from asteroid.models import BaseModel
from kivy.uix.popup import Popup
import os
from model_predict import model_predict
from utils import extract_feature

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
        pos_hint : {'center_y':0.85}
    MDTextField:
        id:username
        pos_hint: {'center_x':0.5,'center_y':0.7}
        size_hint: (0.7,0.1)
        hint_text : 'username'
        helper_text: 'Required'
        helper_text_mode: 'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:dob
        pos_hint: {'center_x':0.5,'center_y':0.6}
        size_hint: (0.7,0.1)
        hint_text : 'Date of Birth'
        helper_text: 'Required in form DD-MM-YYYY'
        helper_text_mode: 'on_focus'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required : True
    MDTextField:
        id:gender
        pos_hint: {'center_x':0.5,'center_y':0.5}
        size_hint: (0.7,0.1)
        hint_text : 'Gender'
        helper_text: 'Man/Female/Other'
        helper_text_mode: 'on_focus'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
    MDTextField:
        id:country
        pos_hint: {'center_x':0.5,'center_y':0.4}
        size_hint: (0.7,0.1)
        hint_text : 'Country'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.2}
        user_font_size: '35sp'
        on_press: app.check_user_details()

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
            app.insertValue()
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
            app.username_changer()
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
        on_press: app.checkDetailsSignin()
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
        text: 'Welcome to Sensound'
        font_style : 'H2'
        halign : 'center'
        pos_hint : {'center_y':0.8}
    MDBoxLayout:
        orientation : 'vertical'
        Image :
            source : "whitelogo.png"
            opacity : .05
            pos_hint: {'center_x': .5,'center_y':0.3}
            size_hint : .7,.7


    MDRaisedButton:
        text: "Upload"
        md_bg_color: app.theme_cls.primary_color
        height: 30
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_release: app.fileChooser()

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


#function that will calculate the age by the date of birth
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
     (birthDate.month, birthDate.day))
    return age


class NewApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(helpstr)
        self.title = 'Sensound'
        return self.strng

    """
    check if the email address is valid and that the field is full.
    if not- than an error window will pop up
    If the mail is already exist in the DB than an error window will pop up
    """
    def checkEmail(self):
        self.email = self.strng.get_screen('emailscreen').ids.email.text
        email_check_false = True
        emailExist = NewApp.checkEmailExist(self)
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
            if emailExist:
                cancel_btn_password_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                self.dialog = MDDialog(title='Email exists', text="This email is already exist in the databas."
                                                                  "\n Please log in or enter another email address",
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_password_dialogue])
                self.dialog.open()
            elif not re.match(email_pattern, self.email):
                cancel_btn_email_dialogue = MDFlatButton(text='Retry', on_release=self.close_email_dialogue)
                self.dialog = MDDialog(title='Invalid Email', text="Please enter a valid Email address",
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_email_dialogue])
                self.dialog.open()
            else:

                self.strng.get_screen('emailscreen').ids.disabled_button.disabled = False


    """
    check that the fields of user name and date of birth are filled
    if not, it will raise an error window.
    this function also check that the user age is above 16.
    country and age fields are allowed
    """
    def check_user_details(self):
        self.username_text = self.strng.get_screen('usernamescreen').ids.username.text
        self.dateBirth = self.strng.get_screen('usernamescreen').ids.dob.text
        self.gender = self.strng.get_screen('usernamescreen').ids.gender.text
        self.country = self.strng.get_screen('usernamescreen').ids.country.text
        valid_gender = ['male', 'Male', 'Female', 'female', 'Other', 'other', '']
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
            splitDob = self.dateBirth.split("-")
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
                self.dialog = MDDialog(title='Invalid Date of birth', text="Please enter a valid date in a DD-MM-YYYY format", size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_username_dialogue])
                self.dialog.open()
            else:
                self.date_time_obj = (datetime.datetime.strptime(self.dateBirth, '%d-%m-%Y')).date()
                if calculateAge(self.date_time_obj) < 16:
                    cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialogue)
                    self.dialog = MDDialog(title='You are not in the right age', text="You must be 16 years old in order to use Sensound",
                                           size_hint=(0.7, 0.2),
                                           buttons=[cancel_btn_username_dialogue])
                    self.dialog.open()
                else:
                    if self.gender in valid_gender:
                        self.strng.get_screen('usernamescreen').ids.disabled_button.disabled = False
                    else:
                        cancel_btn_username_dialogue = MDFlatButton(text='Retry',
                                                                    on_release=self.close_username_dialogue)
                        self.dialog = MDDialog(title='Gender is not valid',
                                               text="You can choose to enter a gender. "
                                                    "\nIf you choose so then fill one of this options: Male/Female/Other."
                                                    "\nElse - keep it empty",
                                               size_hint=(0.7, 0.2),
                                               buttons=[cancel_btn_username_dialogue])
                        self.dialog.open()
    """
    verify that the passwords are the same
    """
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

    """
    returns True if the email is already exist in the DB
    """
    def checkEmailExist(self):
        self.email = self.strng.get_screen('emailscreen').ids.email.text
        email, password = NewApp.getEmailPassSignin(self)
        if self.email == email:
            return True
        else:
            return False
    """
    check that the fields in the sign in window are filled.
    if not- will pop up an error window.
    Also, check if the user mail exists in the DB.
    if Yes- it verify that the password is correct
    if not- will pop up an error window.
    """
    def checkDetailsSignin(self):
        self.email = self.strng.get_screen('signinscreen').ids.email.text
        self.password = self.strng.get_screen('signinscreen').ids.password.text
        email_check_false = True
        self.login_check = False
        try:
            int(self.email)
        except:
            email_check_false = False
        if email_check_false or self.email.split() == [] or self.password.split() ==[]:
            cancel_btn_email_dialogue = MDFlatButton(text='Retry', on_release=self.close_email_dialogue)
            self.dialog = MDDialog(title='These fields are required', text="Please fill all the fields",
                                   size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_email_dialogue])
            self.dialog.open()
        elif self.email and self.password:
            curr_email, curr_password = NewApp.getEmailPassSignin(self)
            if not curr_email:
                cancel_btn_email_dialogue = MDFlatButton(text='Retry', on_release=self.close_email_dialogue)
                self.dialog = MDDialog(title='This email does not exist in the data base', text="Please sign up",
                                       size_hint=(0.7, 0.2),
                                       buttons=[cancel_btn_email_dialogue])
                self.dialog.open()
            else:
                if curr_password == self.password:
                    self.strng.get_screen('signinscreen').ids.disabled_button.disabled = False
                else:
                    cancel_btn_email_dialogue = MDFlatButton(text='Retry', on_release=self.close_email_dialogue)
                    self.dialog = MDDialog(title='Incorrect password', text="Please try again",
                                           size_hint=(0.7, 0.2),
                                           buttons=[cancel_btn_email_dialogue])
                    self.dialog.open()
        else:
            self.login_check = True
            self.strng.get_screen('mainscreen').ids.profile_name.text = f"welcome {NewApp.usernameDetails(self)}"
            self.strng.get_screen('signinscreen').ids.disabled_button.disabled = False

    def close_email_dialogue(self, obj):
        self.dialog.dismiss()

    def close_username_dialogue(self, obj):
        self.dialog.dismiss()

    def username_changer(self):
        conn = NewApp.connectToDB(self)
        mycursor = conn.cursor()
        userNamesql = "SELECT username from sensound.Users where email= %s"
        val = self.email
        mycursor.execute(userNamesql, (val,))
        userName = mycursor.fetchall()
        # self.strng.get_screen('mainscreen').ids.profile_name.text = f"Welcome {userName}"
        if self.login_check:
            self.strng.get_screen('mainscreen').ids.profile_name.text = f"welcome {userName}"

    def usernameDetails(self):
        conn = NewApp.connectToDB(self)
        mycursor = conn.cursor()
        userNamesql = "SELECT username from sensound.Users where email= %s"
        val = self.email
        mycursor.execute(userNamesql, (val,))
        userName = mycursor.fetchall()
        return userName

    def on_start(self):
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.username_changer()
                self.strng.get_screen('mainscreen').manager.current = 'mainscreen'

        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'

    def insertValue(self):
        conn = NewApp.connectToDB(self)
        mycursor = conn.cursor()
        sqlInsert = "INSERT INTO sensound.Users (username, password, email, DateOfBirth, gender, country) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.username_text, self.password1, self.email, self.date_time_obj, self.gender, self.country)
        mycursor.execute(sqlInsert, val)
        conn.commit()
        conn.close()

    def connectToDB(self):
        conn = mysql.connector.connect(user='sensoundAdmin',
                                       host='sensound-mysql.cnlubimbgubt.eu-west-2.rds.amazonaws.com',
                                       password='Technion2022',
                                       database='mysql')
        return conn

    def getEmailPassSignin(self):
        conn = NewApp.connectToDB(self)
        mycursor = conn.cursor()
        select_email = "SELECT email, password from sensound.Users where email= %s"
        val = self.email
        email,password = False, False
        mycursor.execute(select_email, (val,))
        records = mycursor.fetchall()
        if len(records) == 0:
            return email, password
        else:
            for row in records:
                email = row[0]
                password = row[1]
        return email, password

    def dismiss_popup(self):
        self._popup.dismiss()

    def fileChooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        if selection:
            self.wavFile = selection[0]
            if self.wavFile:
                self.model = pickle.load(open("GB_classifier.model", "rb"))
                # model = pickle.load(open("C:\\Users\\USER\Desktop\\Technion\\סמסטר ז\\emotionsAnalyzing\\GB_classifier.model", "rb"))
                features = extract_feature(self.wavFile, mfcc=True, chroma=True, mel=True).reshape(1, -1)
                result = self.model.predict(features)[0]
                self.result = result

                self.emotionInfo = NewApp.identifyEmotion(self)
                NewApp.pop_up_emotion(self)

    def pop_up_emotion(self):
        idx, emotion, header, info = NewApp.identifyEmotion(self)
        self.dialog = MDDialog(title= 'Your current feeling is: ' + emotion, text=header +"\n" +info,
                               size_hint=(0.7, 0.2))
        self.dialog.open()

    def identifyEmotion(self):
        conn = NewApp.connectToDB(self)
        mycursor = conn.cursor()
        val = self.result
        sql = "SELECT * FROM sensound.feelingsInfo where feelingType = %s ORDER BY RAND() LIMIT 1"
        mycursor.execute(sql, (val,))
        records = mycursor.fetchall()
        return list(records[0])

NewApp().run()
# conn.close()
