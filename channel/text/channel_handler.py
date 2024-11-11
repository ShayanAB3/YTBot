from abc import ABC, abstractmethod
from discord.ext.commands import Context

class ChannelHandler(ABC):
    @abstractmethod
    async def handler(self,ctx:Context):
        pass