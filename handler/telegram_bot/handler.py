from telegram.ext import Application
from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def AddRoutes(self,app:Application):
        pass


