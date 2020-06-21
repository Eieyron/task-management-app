from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color
from datetime import datetime

class ColorLabel(Label):
    
    def __init__(self, text, colorlist, *args, **kwargs):

        super().__init__(text=text)
        self.canvas.before.add(Color(*colorlist))
        # self.canvas.ask_update()

class StatusGrid(GridLayout):

    def __init__(self, text, schedule, hasPause=False, *args, **kwargs):

        super().__init__(rows = 2)

        self.text = text
        self.schedule = schedule
        self.schedule[self.text] = {}

        statusClass = Label(text=text)
        lowergrid = GridLayout(cols = 3 if not hasPause else 4)

        startButton = Button(text='start')
        startButton.on_press = self.start_click
        
        endButton = Button(text='end')
        endButton.on_press = self.end_click

        self.statusLabel = Button(
            text='not started yet',
            background_color=(0.45, 0.18, 0.21, 1)
        )
        
        lowergrid.add_widget(startButton)

        if hasPause:
            self.pause_history_number = 0
            pause = Button(text='pause')
            pause.on_press = self.pause_click
            lowergrid.add_widget(pause)

        lowergrid.add_widget(endButton)
        lowergrid.add_widget(self.statusLabel)

        self.add_widget(statusClass)
        self.add_widget(lowergrid)
    
    def start_click(self):
        self.change_status(status='ONGOING')
        self.schedule[self.text]['status'] = 'ONGOING'
        self.schedule[self.text]['start'] = datetime.now()
        self.schedule[self.text]['end'] = None        
        print(self.schedule)

    def pause_click(self):
        # self.schedule[self.text]['history'] = []

        if self.schedule[self.text]['status'] != 'PAUSED':
            self.change_status(status='PAUSED')
            self.schedule[self.text]['status'] = 'PAUSED'
            self.schedule[self.text][self.pause_history_number] = [datetime.now()]

        else:
            self.change_status(status='ONGOING')
            self.schedule[self.text]['status'] = 'ONGOING'
            self.schedule[self.text][self.pause_history_number].append(datetime.now())
            self.pause_history_number += 1

        # pass
        print(self.schedule)

    def end_click(self):
        self.change_status(status='FINISHED')
        self.schedule[self.text]['status'] = 'FINISHED'
        self.schedule[self.text]['end'] = datetime.now()
        print(self.schedule)

    def change_status(self, status):
        self.statusLabel.text = status

# Declare both screens
class MainFunctionScreen(Screen):


    def __init__(self, halt_func=None, *args, **kwargs):


        # initialize self as screen
        super().__init__()
        
        # initialize schedule related objects
        self.schedule = {}

        # initialize components
        outergrid               = GridLayout(rows = 4)

        development_widget      = StatusGrid(text='DEVELOPMENT', schedule=self.schedule, hasPause=True)
        
        testing_widget          = StatusGrid(text='TESTING', schedule=self.schedule, hasPause=True)
        
        documentation_widget    = StatusGrid(text='DOCUMENTATION', schedule=self.schedule, hasPause=True)

        finalize_widget         = GridLayout(cols=2)

        halt_button             = Button(text='HALT')
        if halt_func:
            halt_button.on_press    = halt_func

        finalize_button         = Button(text='FINALIZE')
        finalize_button.on_press = self.finalize

        finalize_widget.add_widget(halt_button)
        finalize_widget.add_widget(finalize_button)

        # add components to outergrid
        outergrid.add_widget(development_widget)
        outergrid.add_widget(testing_widget)
        outergrid.add_widget(documentation_widget)
        outergrid.add_widget(finalize_widget)

        # add components to self
        self.add_widget(outergrid)

    def finalize(self):
        print(self.schedule)
