from discord.ui import View as DiscordView, Item, Modal as DiscordModal
from discord import Interaction
from discord.utils import MISSING

from abc import abstractmethod

from src.ui.view import View
from src.ui.modal.discord.discord_modal import DiscordModal as DiscordModalCustom


class Modal(View):
    def __init__(
            self, 
            *,
            title: str=None,
            items:list[Item] = None,
            timeout: float | None = 180,
            custom_id:str = MISSING
        ):
        self.title = title or self.title
        self.items = items or self.items
        self.timeout = timeout or self.timeout
        self.custom_id = custom_id or self.custom_id
        

    @abstractmethod
    async def on_submit(self,modal:DiscordModal,interaction:Interaction):
        pass

    def get(self) -> DiscordView:
        return DiscordModalCustom(self.title,
                                   self.items,
                                   self.on_submit,
                                   custom_id=self.custom_id,
                                   timeout=self.timeout)