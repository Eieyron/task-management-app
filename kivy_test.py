import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from screens.test_screen import TestScreen

from kivy.uix.screenmanager import ScreenManager, Screen

class TestApp(App):

    def build(self):

        # layout = GridLayout(cols=2)

        # layout.add_widget(Label(text='Hello 1'))
        # layout.add_widget(Label(text='World 1'))
        # layout.add_widget(Label(text='Hello 2'))
        # layout.add_widget(Label(text='World 2'))

        sm = ScreenManager()

        screens = {}

        screens['test'] = TestScreen(name='test')

        sm.switch_to(screens['test'])

        return sm

if __name__ == '__main__':
    TestApp().run()
    