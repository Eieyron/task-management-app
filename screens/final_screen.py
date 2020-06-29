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

        gridlayout = GridLayout(rows=3)

        self.reasonInput = TextInput(text='Enter Halt Reason', multiline=False)

        gridlayout.add_widget(Label(text='Halt Reason'))

        gridlayout.add_widget(self.reasonInput)
        # self.reasonInput.bind(text=self.calc)

        gridlayout.add_widget(Button(text='Resume', size_hint_y=None))

        self.add_widget(gridlayout)

    # def calc(self, instance, text):
    #     print(text)