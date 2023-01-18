from abc import abstractmethod
from src.ui.console_ui import ConsoleUI


class Observer:
    @abstractmethod
    def update(self, message):
        pass


class UIObserver(Observer):
    def __init__(self, ui: ConsoleUI):
        self.__ui = ui

    def update(self, code):
        self.__ui.display_observer_message(code)
