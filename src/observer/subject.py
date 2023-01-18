from abc import abstractmethod


class Subject:
    @abstractmethod
    def attach_observer(self, new_observer):
        pass

    @abstractmethod
    def detach_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, message):
        pass


class GameSubject(Subject):
    def __init__(self):
        self.__observers = []

    def attach_observer(self, new_observer):
        self.__observers.append(new_observer)

    def detach_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, code):
        for observer in self.__observers:
            observer.update(code)

