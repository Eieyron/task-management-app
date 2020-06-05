from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class StatusGrid(GridLayout):

    def __init__(self, text, *args, **kwargs):

        super().__init__(rows = 2)

        statusClass = Label(text=text)
        lowergrid = GridLayout(cols = 3)

        startButton = Button(text='start')
        startButton.on_press = self.start_click
        
        endButton = Button(text='end')
        endButton.on_press = self.end_click

        statusLabel = Label(text='----')

        lowergrid.add_widget(startButton)
        lowergrid.add_widget(endButton)
        lowergrid.add_widget(statusLabel)

        self.add(statusClass)
        self.add(lowergrid)

    def start_click(self):
        pass

    def end_click(self):
        pass

    def change_status(self, status):
        pass

# Declare both screens
class MainFunctionScreen(Screen):

    def __init__(self, *args, **kwargs):

        super().__init__()

        # self.add_widget(Label(text="test"))

        outergrid               = GridLayout(rows = 4)

        development_widget      = StatusGrid(text='development')
        testing_widget          = StatusGrid(text='testing')
        documentation_widget    = StatusGrid(text='documentation')
        halt_button             = Button(text='halt')

        outergrid.add_widget(development_widget)
        outergrid.add_widget(testing_widget)
        outergrid.add_widget(documentation_widget)
        outergrid.add_widget(halt_button)

        self.add_widget(outergrid)
        

    

