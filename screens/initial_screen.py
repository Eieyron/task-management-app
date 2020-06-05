import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from kivy.config import Config
Config.set('graphics', 'width', '290')
Config.set('graphics', 'height', '300')

class InitScrn(App):

    def build(self):

#=======Start Level1 Panel 2=================================================
        lvl2 = GridLayout(rows=3, cols = 2)

        #For Name of Developer
        lvl2.add_widget(Label(text='Developer Name:', ))
        lvl2.add_widget(TextInput(text='Type Name Here', multiline = False))

        #For Change Name
        lvl2.add_widget(Label(text='Change Name: '))
        lvl2.add_widget(TextInput(text='Type Name Here', multiline = False))

        #For Ticket Number
        lvl2.add_widget(Label(text='Ticket Number: '))
        lvl2.add_widget(TextInput(text='Type Number Here', multiline = False))
#=======End Level1 Panel 2====================================================


#=======Start Main Panel======================================================
        lvl1 = GridLayout(rows=3, row_default_height=100)

        lvl1.add_widget(Label(text='Blaze Change Manger', size_hint_y=None))    #Panel 1
        lvl1.add_widget(lvl2)                                                   #Panel 2
        lvl1.add_widget(Button(text='Start Change', size_hint_y=None))           #Panel 3
#=======End Main Panel========================================================

        return lvl1

if __name__ == '__main__':
    InitScrn().run()
    