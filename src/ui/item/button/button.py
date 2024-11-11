from discord.ui import View as DiscordView
from src.ui.item.item import Item
from discord import ButtonStyle, PartialEmoji, Emoji
from typing import Optional, Union
from discord.ui import Button as DiscordButton

class Button(Item):
    def __init__(
        self, 
        style: ButtonStyle = ButtonStyle.secondary,
        label: Optional[str] = None,
        disabled: bool = False,
        custom_id: Optional[str] = None,
        url: Optional[str] = None,
        emoji: Optional[Union[str, Emoji, PartialEmoji]] = None,
        row: Optional[int] = None,
        *, 
        timeout: float | None = 180
    ):
        self.label = label or self.label
        self.style = style or self.style
        self.disabled = disabled or self.disabled
        self.custom_id = custom_id or self.custom_id
        self.url = url or self.url
        self.emoji = emoji or self.emoji
        self.row = row or self.row
        super().__init__(timeout=timeout)

    def get(self) -> DiscordView:
        button = DiscordButton(
            label=self.label,
            style=self.style,
            custom_id=self.custom_id,
            url=self.url,
            disabled=self.disabled,
            emoji=self.emoji,
            row=self.row
        )
        button.callback = self.handler
        self.add_item(button)
        return self