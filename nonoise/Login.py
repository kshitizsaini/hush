from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
class Login(Screen):

    def loginAuthen(self,username,password):
        database = open("MyDataBase.txt", "r")
        flag = 0

        for line in database.readlines():
            array = line.split(",")

            if(array[1] == username.text and array[2] == password.text+"\n"):
                flag = 1
        return flag
