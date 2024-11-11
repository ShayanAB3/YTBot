from discord import Interaction
from src.ui.item.select.select import Select as BaseSelect
from abc import abstractmethod

class Select(BaseSelect):
    """
    :param custom_id: :class:`str`
        The ID of the select menu that gets received during an interaction.
        If not given then one is generated for you.
    :param placeholder: Optional[:class:`str`]
        The placeholder text that is shown if nothing is selected, if any.
    :param min_values: :class:`int`
        The minimum number of items that must be chosen for this select menu.
        Defaults to 1 and must be between 0 and 25.
    :param max_values: :class:`int`
        The maximum number of items that must be chosen for this select menu.
        Defaults to 1 and must be between 1 and 25.
    :param options: List[:class:`discord.SelectOption`]
        A list of options that can be selected in this menu.
    :param disabled: :class:`bool`
        Whether the select is disabled or not.
    :param row: Optional[:class:`int`]
        The relative row this select menu belongs to. A Discord component can only have 5
        rows. By default, items are arranged automatically into those 5 rows. If you'd
        like to control the relative positioning of the row then passing an index is advised.
        For example, row=1 will show up before row=2. Defaults to ``None``, which is automatic
        ordering. The row number must be between 0 and 4 (i.e. zero indexed).
    """
    placeholder:str = ""
    min_values:int = 1
    max_values:int = 1
    options:dict[str,str] = {}

    @abstractmethod
    async def handler(self, interaction: Interaction):
        pass