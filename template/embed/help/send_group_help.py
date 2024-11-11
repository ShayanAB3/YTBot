from typing import Any

from template.embed.embed import Embed

from discord.ext.commands import Group
from discord import Embed as DiscordEmbed

class SendGroupHelp(Embed):
    def template(self, embed: DiscordEmbed, data: dict[str, Any]):
        group:Group = data.get("group")
        for command in group.commands:
            embed.add_field(name=f"`{command.name}`", value=command.help, inline=False)