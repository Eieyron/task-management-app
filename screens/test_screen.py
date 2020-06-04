from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label



# Declare both screens
class TestScreen(Screen):

    def __init__(self, *args, **kwargs):
        
        super().__init__()

        self.add_widget(Label(text="test"))

    

