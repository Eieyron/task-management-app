import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class InitialScreen(Screen):
    
    def __init__(self, changefunction=None, *args, **kwargs):

        super().__init__()

        # self.mainFunctionScreen = mainFunctionScreen

        startChangeButton = Button(text='Start Change', size_hint_y=None)
        startChangeButton.on_press = changefunction

        
#=======Start Level1 Panel 2=================================================
        lvl2 = GridLayout(rows=3, cols = 2)

        self.Name = TextInput(text='Type Name Here', multiline = False)
        # self.Name.bind(text=self.pass_developer_name)

        changeName = TextInput(text='Type Name Here', multiline = False)
        
        self.ticketNumber = TextInput(text='Type Number Here', multiline = False)
        # self.ticketNumber.bind(text=self.pass_ticket_number)

        #For Name of Developer
        lvl2.add_widget(Label(text='Developer Name:', ))
        lvl2.add_widget(self.Name)

        #For Change Name
        lvl2.add_widget(Label(text='Change Name: '))
        lvl2.add_widget(changeName)

        #For Ticket Number
        lvl2.add_widget(Label(text='Ticket Number: '))
        lvl2.add_widget(self.ticketNumber)
#=======End Level1 Panel 2====================================================


#=======Start Main Panel======================================================
        lvl1 = GridLayout(rows=3, row_default_height=100)

        lvl1.add_widget(Label(text='Blaze Change Manger', size_hint_y=None))    #Panel 1
        lvl1.add_widget(lvl2)                                                   #Panel 2
        lvl1.add_widget(startChangeButton)                                      #Panel 3
#=======End Main Panel========================================================
        self.add_widget(lvl1)


    # def pass_developer_name(self, instance, text):

    #     try:
    #         self.mainFunctionScreen.set_user_credentials(text)
    #     except:
    #         pass

    # def pass_ticket_number(self, instance, text):

    #     try:
    #         self.mainFunctionScreen.set_ticket_number(text)
    #     except:
    #         pass
