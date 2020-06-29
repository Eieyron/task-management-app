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
from screens.scheduler import Scheduler

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '450')

class MgmntApp(App, Scheduler):

	sm = ScreenManager()
	scrn = Screen()

	def build(self):

		self.screens = {}

		self.screens['Initial Screen'] = InitialScreen(
			changefunction		=	self.switch_second_screen, 
		)

		self.screens['Main Function Screen'] = MainFunctionScreen(
			halt_func			=	self.switch_final_screen,
			finalize_func		=	self.switch_final_screen,
			init_screen 		=   self.screens['Initial Screen'] 
		)

		self.screens['Final Screen'] = FinalScreen()


		self.sm.switch_to(self.screens['Initial Screen'])

		return self.sm

	def switch_second_screen(self):
		self.sm.switch_to(self.screens['Main Function Screen'])
		print(self.sm.screens[0].developerName.text)

	def switch_final_screen(self):
		self.sm.switch_to(self.screens['Final Screen'])


if __name__ == '__main__':
    MgmntApp().run()