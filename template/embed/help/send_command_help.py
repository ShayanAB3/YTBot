from typing import Any

from template.embed.embed import Embed

from discord.ext.commands import Command, HelpCommand
from discord import Embed as DiscordEmbed

class SendCommandHelp(Embed):
    command:Command
    help:HelpCommand

    def template(self, embed: DiscordEmbed, data: dict[str, Any]):
        command:Command = self.command
        help:HelpCommand = self.help

        if command.cog_name:
            embed.add_field(name="Cog:",value=command.cog_name, inline=False)
        
        if command.parent:
            embed.add_field(name="Parent:",value=command.parent, inline=False)

        if command.aliases:
            embed.add_field(name="Aliases:", value=", ".join(command.aliases), inline=False)

        embed.add_field(name="Command usage:", value=f"`{help.get_command_signature(command)}`", inline=False)