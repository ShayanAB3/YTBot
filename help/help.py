from typing import Mapping

from discord.ext.commands import HelpCommand
from discord.ext.commands import Cog, Group, Command

from template.embed.help.send_bot_help import SendBotHelp
from template.embed.help.send_cog_help import SendCogHelp
from template.embed.help.send_group_help import SendGroupHelp
from template.embed.help.send_command_help import SendCommandHelp

class Help(HelpCommand):
    
    async def send_bot_help(self, mapping: Mapping):
        embed = SendBotHelp(title="Bot Commands", description="Here are all the commands available:")
        embed.mapping = mapping
        channel = self.get_destination()
        await channel.send(embed=embed.get())
    
    async def send_cog_help(self, cog: Cog):
        embed = SendCogHelp(title=f"{cog.qualified_name} Commands", description=cog.description)
        embed.set({"cog":cog})
        channel = self.get_destination()
        await channel.send(embed=embed.get())
    
    async def send_group_help(self, group: Group):
        embed = SendGroupHelp(title=f"{group.name} Group Commands", description=group.help)
        embed.set({"group": group})
        channel = self.get_destination()
        await channel.send(embed=embed.get())
    
    async def send_command_help(self, command: Command):
        embed = SendCommandHelp(title=f"{command.name} Command", description=command.help)
        embed.set({"command":command,"help":self})
        channel = self.get_destination()
        await channel.send(embed=embed.get())

