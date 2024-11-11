from typing import Any
from template.embed.embed import Embed
from typing import Any, Mapping
from discord import Embed as DiscordEmbed

class SendBotHelp(Embed):
    mapping:Mapping

    def template(self, embed: DiscordEmbed, data: dict[str, Any]):
        for cog, commands in self.mapping.items():
            if commands:
                cog_name = getattr(cog, "qualified_name", "No Category")
                command_list = "\n".join([f"`{command.name}`: {command.help}" for command in commands])
                embed.add_field(name=cog_name, value=command_list, inline=False)
