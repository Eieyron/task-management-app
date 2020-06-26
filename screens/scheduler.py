from screens.initial_screen import InitialScreen
from screens.main_function_screen import MainFunctionScreen
from screens.final_screen import FinalScreen


class Scheduler(InitialScreen, MainFunctionScreen, FinalScreen):

		developerData = InitialScreen()
		logData = MainFunctionScreen()

		developerData.developerName.text
		developerData.changeName.text
		developerData.ticketNumber.text

		logData.schedule