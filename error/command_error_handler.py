from abc import ABC, abstractmethod
from discord.ext.commands import Context
from discord import Interaction
from typing_extensions import Union

class CommandErrorHandler(ABC):
    @abstractmethod
    async def handler(self,command:Union[Context,Interaction], error:Exception):
        pass