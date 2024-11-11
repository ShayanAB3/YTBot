from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from discord import Embed as DiscordEmbed , Color
from discord.types.embed import EmbedType


class Embed(ABC):        
    data:dict[str,Any] = {}
    """
    This default settings
        :param title: The title of the embedded message.
        :param description: Description of the embedded message.
        :param colour: Colour British named.Sets the color of the inline message border.
        :param color: Sets the color of the inline message border.
        :param type: Type of embed (always “rich” for webhook embeds)
            @deprecated
            Embed types should be considered deprecated and might be removed in a future API version
        :param url: Sets the URL for images or links in various inline message methods.
        :param timestamp: The time displayed in the lower right corner of the message. Optional. Can be a datetime object or an ISO 8601 string.
    """
    def __init__(self, *, colour: int | Color = None, 
                 color: int | Color = None, 
                 title: str = None, 
                 type:EmbedType = None, 
                 url: str = None, 
                 description: str = None, 
                 timestamp: datetime = None):
        
        self.colour = colour or self.colour
        self.color = color or self.color
        self.title = title or self.title
        self.type = type or self.type
        self.url = url or self.url
        self.description = description or self.description
        self.timestamp = timestamp or self.timestamp
        
    @abstractmethod
    def template(self,embed:DiscordEmbed,data:dict[str,Any]):
        pass
    
    def get(self) -> DiscordEmbed:
        embed = DiscordEmbed(colour=self.colour, 
                                  color=self.color, 
                                  title=self.title, 
                                  type=self.type, 
                                  url=self.url, 
                                  description=self.description, 
                                  timestamp=self.timestamp)
        self.template(embed=embed,data=self.data)
        return embed

    def set(self,data:dict[str,Any]):
        self.data.update(data)
