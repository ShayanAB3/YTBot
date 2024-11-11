from discord import ButtonStyle, PartialEmoji, Interaction
from src.ui.item.button.button import Button as BaseButton
from abc import abstractmethod
from typing import Optional

class Button(BaseButton):
    """
    :param style: :class:`discord.ButtonStyle`
        The style of the button.
    :param custom_id: Optional[:class:`str`]
        The ID of the button that gets received during an interaction.
        If this button is for a URL, it does not have a custom ID.
    :param url: Optional[:class:`str`]
        The URL this button sends you to.
    :param disabled: :class:`bool`
        Whether the button is disabled or not.
    :param label: Optional[:class:`str`]
        The label of the button, if any.
    :param emoji: Optional[Union[:class:`.PartialEmoji`, :class:`.Emoji`, :class:`str`]]
        The emoji of the button, if available.
    :param row: Optional[:class:`int`]
        The relative row this button belongs to. A Discord component can only have 5
        rows. By default, items are arranged automatically into those 5 rows. If you'd
        like to control the relative positioning of the row then passing an index is advised.
        For example, row=1 will show up before row=2. Defaults to ``None``, which is automatic
        ordering. The row number must be between 0 and 4 (i.e. zero indexed).
    """
    label: Optional[str] = ""
    style:ButtonStyle = ButtonStyle.primary
    custom_id: Optional[str] = None
    url: Optional[str] = None
    disabled: bool = False
    emoji: Optional[PartialEmoji] = None
    row: Optional[int] = None

    @abstractmethod
    async def handler(self, interaction: Interaction):
        pass