from typing import Any

from template.embed.embed import Embed

from discord.ext.commands import Command, HelpCommand
from discord import Embed as DiscordEmbed

class SendCommandHelp(Embed):
    def template(self, embed: DiscordEmbed, data: dict[str, Any]):
        command:Command = data.get("command")
        help:HelpCommand = data.get("help")
        if command.aliases:
            embed.add_field(name="Aliases", value=", ".join(command.aliases), inline=False)
        embed.add_field(name="Usage", value=f"`{help.get_command_signature(command)}`", inline=False)