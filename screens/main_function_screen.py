from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color

class ColorLabel(Label):
    
    def __init__(self, text, colorlist, *args, **kwargs):

        super().__init__(text=text)
        self.canvas.before.add(Color(*colorlist))
        # self.canvas.ask_update()

class StatusGrid(GridLayout):

    def __init__(self, text, *args, **kwargs):

        super().__init__(rows = 2)

        statusClass = Label(text=text)
        lowergrid = GridLayout(cols = 3)

        startButton = Button(text='start')
        startButton.on_press = self.start_click
        
        endButton = Button(text='end')
        endButton.on_press = self.end_click

        self.statusLabel = Button(
            text='not started yet',
            background_color=(0.45, 0.18, 0.21, 1)
        )

        lowergrid.add_widget(startButton)
        lowergrid.add_widget(endButton)
        lowergrid.add_widget(self.statusLabel)

        self.add_widget(statusClass)
        self.add_widget(lowergrid)

    def start_click(self):
        self.change_status(status='ongoing')

    def end_click(self):
        self.change_status(status='finished')

    def change_status(self, status):
        self.statusLabel.text = status

# Declare both screens
class MainFunctionScreen(Screen):

    def __init__(self, haltfunction=None, *args, **kwargs):

        # initialize self as screen
        super().__init__()

        # initialize components
        outergrid               = GridLayout(rows = 4)

        development_widget      = StatusGrid(text='DEVELOPMENT')
        
        testing_widget          = StatusGrid(text='TESTING')
        
        documentation_widget    = StatusGrid(text='DOCUMENTATION')

        halt_button             = Button(text='HALT')
        if haltfunction:
            halt_button.on_press = haltfunction

        # # add components to outergrid
        outergrid.add_widget(development_widget)
        outergrid.add_widget(testing_widget)
        outergrid.add_widget(documentation_widget)
        outergrid.add_widget(halt_button)

        # # add components to self
        self.add_widget(outergrid)
        

    

