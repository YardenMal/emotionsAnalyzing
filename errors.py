import re
import datetime
from datetime import date
import mysql.connector
curremail="yardefgdn@gmail.com"
# Connecting from the server
conn = mysql.connector.connect(user='sensoundAdmin',
                               host='sensound-mysql.cnlubimbgubt.eu-west-2.rds.amazonaws.com',
                               password='Technion2022',
                               database='mysql')
mycursor = conn.cursor()
sql = "SELECT email,password from sensound.Users where email= %s"
val = curremail
mycursor.execute(sql, (val,))
records = mycursor.fetchall()
for row in records:
    email=row[0]
    password2= row[1]

def checkEmailExists():
    conn = mysql.connector.connect(user='sensoundAdmin',
                                   host='sensound-mysql.cnlubimbgubt.eu-west-2.rds.amazonaws.com',
                                   password='Technion2022',
                                   database='mysql')
    mycursor = conn.cursor()
    select_email = "SELECT email, password from sensound.Users where email= %s"
    val = "yardedhdhdn@gmail.com"
    mycursor.execute(select_email, (val,))
    records = mycursor.fetchall()
    if len(records)==0:
        return 0
    else:
        for row in records:
            email = row[0]
            password2 = row[1]
    return email,password2
# print(email, password2)
print(checkEmailExists())
# Disconnecting from the server
conn.close()
# pattern = r'^[A-Z a-z 0-9]+[\._]?[A-Z a-z 0-9]+[@]\w+[.]\w{2,3}$'
pat = "^[a-zA-Z0-9-_]+[\._]?[A-Z a-z 0-9]+@[a-zA-Z0-9]+\.[a-z]+[\._]?[a-z]{2,3}$"
class LoginError:
    CAUSE = ""

    def print_error(self, details):
        print(self.CAUSE.format(*details))


class WrongEmailError(LoginError):
    CAUSE = "Email {} not found."


class PasswordMismatch(LoginError):
    CAUSE = "Password {} does not match password {}"


def main():
    email1 = "yarden.as@gmail.co.il"
    email = "popular_website15@comPany.com"
    p1 = "123PassWord"
    p2 = "123pass_word"

    if re.match(pat, email):
        print("Valid email")
    else:
        e1 = WrongEmailError()
        e1.print_error([email])
    e2 = PasswordMismatch()

    e2.print_error([p1, p2])


# if __name__ == "__main__":
#     main()

dob = '01/01/2000'
trying="g"
date_time_obj = (datetime.datetime.strptime(dob, '%d/%m/%Y')).date()

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <
     (birthDate.month, birthDate.day))
    return age

def checkage(age):
    splitDob = age.split("/")
    s = [str(integer) for integer in splitDob]
    a_string = "".join(s)
    print(splitDob)
    # for i in range(len(splitDob)):
    #     if a_string[i] == "0":
    #         if i ==0:
    #             new_string = int(a_string[i+1:])
    # if a_string.isalpha() or not isinstance(new_string, int):
    if a_string.isalpha():
        print("Yarden")

    else:
        username_age_false = False
        print("almog")


def what(gender):
    valid_gender = ['man', 'Man', 'Female', 'female', 'Other', 'other', '']
    if gender in valid_gender:
        print("great")
    else:
        print("not gender")


# if str(type((datetime.datetime.strptime(trying, '%d/%m/%Y')).date())) != "<class 'datetime.date'>":
#     print("BYE")
# else:
#     print("GOOD")

def dateB(datebd):
    date_check_false = True
    try:
        (datetime.datetime.strptime(dob, '%d/%m/%Y')).date()
    except ValueError:
        print("not good")
        date_check_false = False
    # if date_check_false:
    #     print("not good")
    # else:
    #     print(date_time_obj)


import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

# sample_rate, samples = wavfile.read('03-01-01-01-01-02-02.wav')
# print(sample_rate, type(sample_rate), samples, type(samples))
# frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
'''
< MainScreen >:
name: 'mainscreen'
MDLabel:
id: profile_name
text: 'main screen'
font_style: 'H2'
halign: 'center'
pos_hint: {'center_y': 0.7}
MDBoxLayout:
orientation: 'vertical'
spacing: 50
space_x: self.size[0] / 3
canvas.before:
Color:
rgba: (0, 0, 0, 0)
Rectangle:
size: self.size
pos: self.pos
Image:
source: "whitelogo.png"
opacity: .05
pos_hint: {'center_x': .5, 'center_y': 0.3}
size_hint: .7, .7

FloatLayout:
orientation: 'vertical'
padding: 100
spacing: 30
BoxLayout:
Button:
text: 'Load'
bold: True
# on_release: app.show_load()
size_hint: 0.6, 0.1
Button:
text: 'Save'
bold: True
size_hint: 0.6, 0.1
# on_release: app.show_save()
BoxLayout:
TextInput:
id: text_input
text: ''

RstDocument:
text: text_input.text
show_errors: True
# 
# <LoadDialog>:
#     BoxLayout:
#         size: app.size
#         pos: app.pos
#         orientation: "vertical"
#         FileChooserListView:
#             id: filechooser
# 
#         BoxLayout:
#             size_hint_y: None
#             height: 30
#             Button:
#                 text: "Cancel"
#                 on_release: app.cancel()
# 
#             Button:
#                 text: "Load"
#                 on_release: app.load(filechooser.path, filechooser.selection)
# 
# <SaveDialog>:
#     text_input: text_input
#     BoxLayout:
#         size: app.size
#         pos: app.pos
#         orientation: "vertical"
#         FileChooserListView:
#             id: filechooser
#             on_selection: text_input.text = self.selection and self.selection[0]
'''
