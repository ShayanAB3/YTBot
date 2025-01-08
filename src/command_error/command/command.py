from discord.ext.commands import Context
from discord import Interaction

from typing_extensions import Union

from abc import ABC, abstractmethod

class Command(ABC):
    command:Union[Context,Interaction]
    def __init__(self,command:Union[Context,Interaction]):
        self.command = command
    
    @abstractmethod
    async def execute_not_found_exceptions(self,error:Exception):
        pass
    
    @abstractmethod
    async def send(self, message:str,**kwargs):
        pass