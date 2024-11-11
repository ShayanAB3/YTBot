from discord import Interaction
from discord.ui import Modal, Item
from discord.utils import MISSING

from collections.abc import Callable


class DiscordModal(Modal):
    on_submit_callback:Callable[[Modal,Interaction],None]

    def __init__(
            self, 
            title: str,
            items: list[Item], 
            on_submit:Callable[[Modal,Interaction],None],
            *,
            custom_id:str = MISSING,
            timeout: float | None = None):
        super().__init__(title=title,
                         custom_id=custom_id,
                         timeout=timeout)
        for item in items:
            self.add_item(item)
        self.on_submit_callback = on_submit

    async def on_submit(self, interaction: Interaction):
        await self.on_submit_callback(self,interaction)