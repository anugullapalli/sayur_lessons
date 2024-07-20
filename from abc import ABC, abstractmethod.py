from abc import ABC, abstractmethod

#Abstract base class
class LibraryItem(ABC):
    @abstractmethod
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def display(self):
        pass


