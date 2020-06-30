from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color
from datetime import datetime
import pickle

class ColorLabel(Label):
    
    def __init__(self, text, colorlist, *args, **kwargs):

        super().__init__(text=text)
        self.canvas.before.add(Color(*colorlist))
        # self.canvas.ask_update()

class StatusGrid(GridLayout):

    def __init__(self, text, parent_screen, hasPause=False, *args, **kwargs):

        super().__init__(rows = 2)

        self.text = text
        # self.schedule = parent_screen.schedule
        self.parent_screen = parent_screen
        self.parent_screen.schedule[self.text] = {
            'status' : 'default'
        }

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
            self.pause = Button(text='pause')
            self.pause.on_press = self.pause_click
            lowergrid.add_widget(self.pause)

        lowergrid.add_widget(endButton)
        lowergrid.add_widget(self.statusLabel)

        self.add_widget(statusClass)
        self.add_widget(lowergrid)
    
    def start_click(self):

        if self.text == 'TESTING':
            if self.parent_screen.development_widget.schedule['DEVELOPMENT']['status'] != 'ONGOING':
                return
        elif self.text == 'DOCUMENTATION':
            if self.parent_screen.testing_widget.schedule['TESTING']['status'] != 'ONGOING':
                return

        if self.parent_screen.schedule[self.text]['status'] in ['default']:
            self.change_status(status='ONGOING')
            self.parent_screen.schedule[self.text]['status'] = 'ONGOING'
            self.parent_screen.schedule[self.text]['start'] = datetime.now()
            self.parent_screen.schedule[self.text]['logs'] = []        
            self.parent_screen.schedule[self.text]['end'] = None        
        
        print(self.parent_screen.schedule)

    def pause_click(self):

        if self.parent_screen.schedule[self.text]['status'] in ['ONGOING']:
            self.change_status(status='PAUSED')
            self.pause.text = 'resume'
            self.parent_screen.schedule[self.text]['status'] = 'PAUSED'
            self.parent_screen.schedule[self.text]['logs'].append([datetime.now()])

        elif self.parent_screen.schedule[self.text]['status'] in ['PAUSED']:
            self.pause.text = 'pause'
            self.change_status(status='ONGOING')
            self.parent_screen.schedule[self.text]['status'] = 'ONGOING'
            self.parent_screen.schedule[self.text]['logs'][self.pause_history_number].append(datetime.now())
            self.pause_history_number += 1

        # pass
        print(self.parent_screen.schedule)

    def end_click(self):

        if self.parent_screen.schedule[self.text]['status'] in ['ONGOING']:

            self.change_status(status='FINISHED')
            self.parent_screen.schedule[self.text]['status'] = 'FINISHED'
            self.parent_screen.schedule[self.text]['end'] = datetime.now()
            print(self.parent_screen.schedule)

    def change_status(self, status):
        self.statusLabel.text = status

# Declare both screens
class MainFunctionScreen(Screen):

    def __init__(self, halt_func=None, finalize_func=None, init_screen=None, *args, **kwargs):

        # initialize self as screen
        super().__init__()
        
        # initialize schedule related objects
        self.user_credentials = {
            "username" : "default",
            "ticketno" : "default",
        }
        self.schedule = {}
        self.init_screen = init_screen


        # initialize components
        outergrid                   = GridLayout(rows = 5)

        namegrid                    = GridLayout(cols = 2)
        self.usernamelabel          = Label(text=self.user_credentials['username'])
        self.ticketnolabel          = Label(text=self.user_credentials['ticketno'])

        self.development_widget     = StatusGrid(
            text='DEVELOPMENT', 
            parent_screen=self, 
            hasPause=True
        )
        
        self.testing_widget         = StatusGrid(
            text='TESTING', 
            parent_screen=self, 
            hasPause=True
        )
        
        self.documentation_widget   = StatusGrid(
            text='DOCUMENTATION', 
            parent_screen=self, 
            hasPause=True
        )

        self.finalize_widget        = GridLayout(cols=2)

        halt_button                 = Button(text='HALT')
        if halt_func:
            self.halt_func          = halt_func
            halt_button.on_press    = self.press_halt

        finalize_button             = Button(text='FINALIZE')
        if finalize_func:
            self.finalize_func          = finalize_func
            finalize_button.on_press    = self.press_finalize

        self.finalize_widget.add_widget(halt_button)
        self.finalize_widget.add_widget(finalize_button)

        # add components to namegrid
        namegrid.add_widget(self.usernamelabel)
        namegrid.add_widget(self.ticketnolabel)

        # add components to outergrid
        outergrid.add_widget(namegrid)
        outergrid.add_widget(self.development_widget)
        outergrid.add_widget(self.testing_widget)
        outergrid.add_widget(self.documentation_widget)
        outergrid.add_widget(self.finalize_widget)

        # add components to self
        self.add_widget(outergrid)

    def set_user_credentials(self, username):
        self.user_credentials["username"] = username
        self.usernamelabel.text = username

    def set_ticket_number(self, ticketno):
        self.user_credentials["ticketno"] = ticketno
        self.ticketnolabel.text = ticketno

    def on_pre_enter(self, *args):
        self.set_user_credentials(self.init_screen.developerName.text)
        self.set_ticket_number(self.init_screen.ticketNumber.text)
        self.load()

    def set_schedule(self, loaded_schedule):

        print(loaded_schedule)
        # print(loaded_schedule['DEVELOPMENT']['status'])
        self.development_widget.change_status(loaded_schedule['DEVELOPMENT']['status'])
        self.testing_widget.change_status(loaded_schedule['TESTING']['status'])
        self.documentation_widget.change_status(loaded_schedule['DOCUMENTATION']['status'])

        self.schedule = loaded_schedule
    
    def press_halt(self):
        self.halt_func()
        self.save()

    def press_finalize(self):
        self.finalize_func()
        self.save()
    
    def save(self):
        
        print(self.schedule)

        file = open("users/"+self.user_credentials["username"]+"_"+self.user_credentials["ticketno"]+".dump", "wb")

        pickle.dump(self.schedule, file)

        file.close()

        print('profile saved.')

    def load(self):

        try:
            file = open("users/"+self.user_credentials["username"]+"_"+self.user_credentials["ticketno"]+".dump", "rb")

            loaded_schedule = pickle.load(file)
            self.set_schedule(loaded_schedule)

            file.close()

            print("successfully loaded previous schedule")
        except Exception as e:
            # print(e.__class__)
            if isinstance(e, FileNotFoundError):
                print(e)
            else:
                print(e.__class__)
                print(e)



    