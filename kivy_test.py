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

        # layout = GridLayout(cols=2)

        # layout.add_widget(Label(text='Hello 1'))
        # layout.add_widget(Label(text='World 1'))
        # layout.add_widget(Label(text='Hello 2'))
        # layout.add_widget(Label(text='World 2'))

        test = Screen()

        self.sm = ScreenManager()

        self.screens = {}

        self.screens['test'] = MainFunctionScreen(haltfunction=self.switch_screen)
        self.screens['test2'] = test
        self.screens['testfunc'] = self.test_func

        self.screens['testfunc']()

        self.sm.switch_to(self.screens['test'])


        return self.sm

    def switch_screen(self):
        self.sm.switch_to(self.screens['test2'])

    def test_func(self):
        print('test')

if __name__ == '__main__':
    TestApp().run()
    