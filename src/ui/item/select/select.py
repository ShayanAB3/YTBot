from discord.ui import Select as DiscordSelect, View as DiscordView
from discord import SelectOption
from src.ui.item.item import Item

class Select(Item):    
    def __init__(
            self, 
            placeholder:str ="",
            min_values:int = 1,
            max_values:int = 1,
            options: dict[str,str]={},*, timeout: float | None = 180
        ):
        self.placeholder = placeholder or self.placeholder 
        self.min_values = min_values or self.min_values
        self.max_values = max_values or self.max_values
        self.options = options or self.options
        super().__init__(timeout=timeout)

    def generate_select_option(self) -> list[SelectOption]:
        return [SelectOption(label=key,description=value) for key, value in self.options.items()]

    def get(self) -> DiscordView:
        select = DiscordSelect(
            placeholder=self.placeholder,
            min_values=self.min_values,
            max_values=self.max_values,
            options=self.generate_select_option()
        )
        select.callback = self.handler
        self.add_item(select)
        return self

        