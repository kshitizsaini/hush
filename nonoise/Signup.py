from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Signup(Screen):

    def signupAuthen(self,email,username,password,confirm):
        database = open("MyDataBase.txt","r")
        flag = 0
        if(password.text == confirm.text):
            for line in database.readlines():
                array = line.split(",")
                if array[0] == email.text or array[1] == username.text:
                    flag = 1
        database.close()
        if flag == 0:
            database1 = open("MyDataBase.txt","a")
            database1.write(email.text+","+username.text+","+password.text+"\n")
            database1.close()
            flag = 2
        return flag

