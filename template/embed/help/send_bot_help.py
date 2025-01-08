from template.embed.embed import Embed

from typing import Any, Mapping

from discord import Embed as DiscordEmbed
from discord.ext.commands import Cog
from discord.ext.commands.core import Command


class SendBotHelp(Embed):
    mapping:Mapping[Cog,list[Command]]

    def template(self, embed: DiscordEmbed, data: dict[str, Any]):
        for cog, commands in self.mapping.items():
            if not commands:
                continue
            cog_name = f"Cogs: {cog.qualified_name}" if cog else "Commands without categories:"
            command_list = "\n".join([f"`{command.name}`: {command.help}" for command in commands])
            embed.add_field(name=cog_name, value=command_list, inline=False)
