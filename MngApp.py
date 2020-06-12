import kivy

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

from screens.initial_screen import InitialScreen
from screens.main_function_screen import MainFunctionScreen
from screens.final_screen import FinalScreen

from kivy.config import Config
Config.set('graphics', 'width', '290')
Config.set('graphics', 'height', '300')

class MgmntApp(App):

    def build(self):
    	self.sm = ScreenManager()
    	scrn = Screen()

    	self.screens = {}

    	self.screens['Initial Screen'] = InitialScreen(changefunction=self.switch_second_screen)
    	self.screens['Main Function Screen'] = MainFunctionScreen(haltfunction=self.switch_final_screen)
    	self.screens['Final Screen'] = FinalScreen()

    	self.sm.switch_to(self.screens['Initial Screen'])

    	return self.sm

    def switch_second_screen(self):
    	self.sm.switch_to(self.screens['Main Function Screen'])

    def switch_final_screen(self):
    	self.sm.switch_to(self.screens['Final Screen'])



if __name__ == '__main__':
    MgmntApp().run()