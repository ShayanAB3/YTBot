from abc import ABC, abstractmethod
from discord.ext.commands import Context

class CommandErrorHandler(ABC):
    @abstractmethod
    async def handler(self,ctx:Context, error:Exception):
        pass