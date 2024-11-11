from abc import ABC, abstractmethod
from route.facade.middleware import Middleware

class Command(ABC):
    @abstractmethod
    def command(self,name:str,description:str,middleware:str=""):
        pass