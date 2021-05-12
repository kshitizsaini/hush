from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.base import runTouchApp

from Intro import Intro
from Login import Login
from Signup import Signup
from ProbLogin import ProbLogin
from WindowsManager import WindowsManager
from Safemode import Safemode
from Manualmode import Manualmode
class MyMainApp(App):

    def build(self):
        kv = Builder.load_file("my.kv")
        sm = WindowsManager()
        sm.add_widget(Intro())
        sm.add_widget(Login())
        sm.add_widget(Signup())
        sm.add_widget(ProbLogin())
        sm.add_widget(Safemode())
        sm.add_widget(Manualmode())
        return sm

if __name__ == '__main__':
    MyMainApp().run()
