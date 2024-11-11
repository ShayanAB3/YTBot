from abc import abstractmethod
from discord import Interaction
from src.ui.view import View

class Item(View):
    @abstractmethod
    async def handler(self,interaction:Interaction):
        pass