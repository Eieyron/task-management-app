# kivy_test.py

import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class TestApp(App):

    def build(self):

        layout = GridLayout(cols=2)

        layout.add_widget(Label(text='Hello 1'))
        layout.add_widget(Label(text='World 1'))
        layout.add_widget(Label(text='Hello 2'))
        layout.add_widget(Label(text='World 2'))

        return layout

if __name__ == '__main__':
    TestApp().run()
    