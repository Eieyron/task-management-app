import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from screens.test_screen import TestScreen

from kivy.uix.screenmanager import ScreenManager, Screen

class InitScrn(App):

    def build(self):


        lvl2 = GridLayout(rows=3, cols = 2)

        lvl2.add_widget(Label(text='Panel2-1'))
        lvl2.add_widget(TextInput(text='Panel2-2', multiline = False))
        lvl2.add_widget(Label(text='Panel2-3'))
        lvl2.add_widget(TextInput(text='Panel2-4', multiline = False))
        lvl2.add_widget(Label(text='Panel2-5'))
        lvl2.add_widget(TextInput(text='Panel2-6', multiline = False))

        lvl1 = GridLayout(rows=3)

        lvl1.add_widget(Label(text='Panel1'))
        lvl1.add_widget(lvl2)
        lvl1.add_widget(Button(text='Panel3'))


        return lvl1

if __name__ == '__main__':
    InitScrn().run()
    