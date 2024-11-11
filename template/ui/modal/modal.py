from src.ui.modal.modal import Modal as BaseModal

from abc import abstractmethod

from discord.ui import Item, Modal as DiscordModal
from discord.utils import MISSING
from discord import Interaction

class Modal(BaseModal):
    """
    :param title: :class:`str`
        The title of the modal. Can only be up to 45 characters.
    :param items:
        Contains a list of elements. `Discord.UI` components. For example `Text`, `Button`, `Select`.
    :param timeout: Optional[:class:`float`]
        Timeout in seconds from last interaction with the UI before no longer accepting input.
        If ``None`` then there is no timeout.
    :param custom_id: :class:`str`
        The ID of the modal that gets received during an interaction.
        If not given then one is generated for you.
        Can only be up to 100 characters.
    """
    title:str
    items:list[Item]
    timeout: float | None = 180,
    custom_id:str = MISSING

    @abstractmethod
    async def on_submit(self,modal:DiscordModal,interaction:Interaction):
        pass
    