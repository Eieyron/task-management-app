import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from screens.main_function_screen import MainFunctionScreen

from kivy.uix.screenmanager import ScreenManager, Screen

class TestApp(App):

    def build(self):

        test = Screen()

        self.sm = ScreenManager()

        self.screens = {}

        self.screens['test'] = MainFunctionScreen(misc_func=self.switch_screen)
        self.screens['test2'] = test
        # self.screens['testfunc'] = self.test_func

        self.sm.switch_to(self.screens['test'])

        # fetch user attributes
        init_obj = {
            'developer_name':   "aaron",
            'ticket_number' :   123,
        }

        # sample function call to go to mainfunction screen
        self.go_to_main_functions(
            main_func = MainFunctionScreen(init_obj=init_obj)
        )

        return self.sm

    def switch_screen(self):
        self.sm.switch_to(self.screens['test2'])

    # sample function to go to mainfunction screen
    def go_to_main_functions(self, main_func):
        
        self.screens['mainfunc'] = main_func

        self.sm.switch_to(self.screens['mainfunc'])

    def test_func(self):
        print('test')

if __name__ == '__main__':
    TestApp().run()
    