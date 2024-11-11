from abc import ABC, abstractmethod
from typing import Union

from discord.ext.commands.context import Context
from discord import Interaction

class Middleware(ABC):
    @abstractmethod
    async def handler(self, command:Context) -> bool | None:
        pass

    @abstractmethod
    async def failed_handler(self, command:Context):
        pass