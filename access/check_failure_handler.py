from abc import ABC, abstractmethod
from discord.ext.commands import CommandError,Context
from src.reason.reason import Reason

class CheckFailureHandler(ABC):
    @abstractmethod
    def reason(self) -> Reason:
        pass
    
    @abstractmethod
    def handler(self,ctx:Context,error:CommandError):
        pass