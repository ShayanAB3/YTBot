from discord.ui import View as DiscordView
from abc import ABC, abstractmethod

class View(ABC,DiscordView):
    @abstractmethod
    def get(self) -> DiscordView:
        pass