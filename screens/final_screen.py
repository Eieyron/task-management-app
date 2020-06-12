import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class FinalScreen(Screen):

    def __init__(self, changefunction=None, *args, **kwargs):

        super().__init__()

        gridlayout = GridLayout(rows=1)

        gridlayout.add_widget(Button(text='Publish', size_hint_y=None))

        self.add_widget(gridlayout)