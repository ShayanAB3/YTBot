from typing import Any
from discord import Embed as DiscordEmbed
from template.embed.embed import Embed
from discord.ext.commands import Cog

class SendCogHelp(Embed):
    def template(self, embed: DiscordEmbed, data: dict[str, Any]):
        cog: Cog = data.get("cog")
        for command in cog.get_commands():
            embed.add_field(name=f"`{command.name}`", value=command.help, inline=False)