from src.template.embed.embed import Embed as BaseEmbed
from discord import Color
from discord.types.embed import EmbedType
from datetime import datetime

class Embed(BaseEmbed):
    """
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
    colour: int | Color = None
    color: int | Color = None
    title: str = None
    type:EmbedType = 'rich'
    url: str = None
    description: str = None
    timestamp: datetime = None