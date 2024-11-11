from typing import Any
from template.embed.embed import Embed
from discord import Embed as DiscordEmbed

class Example(Embed):
    def template(self, embed: DiscordEmbed, data: dict[str, Any]):
        embed.add_field(name="Поле 1", value="`Кодовый блок` в поле 1", inline=False)
        embed.add_field(name="Поле 2", value="Значение поля 2", inline=True)
        embed.set_footer(text="Нижний колонтитул")
        embed.set_thumbnail(url=data.get("thumbnail"))
        embed.set_image(url=data.get("image"))