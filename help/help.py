from typing import Mapping

from discord.ext.commands import HelpCommand
from discord.ext.commands import Cog, Group, Command

from template.embed.help.send_bot_help import SendBotHelp
from template.embed.help.send_cog_help import SendCogHelp
from template.embed.help.send_group_help import SendGroupHelp
from template.embed.help.send_command_help import SendCommandHelp



class Help(HelpCommand):
    
    """
    Sends a help message listing all available bot commands.
    
    This command sends an embed containing all the commands that the bot has.
    It formats the available commands and displays them in a neat and readable way.
    
    Command: help    
    """
    async def send_bot_help(self, mapping: Mapping[Cog,list[Command]]):
        embed = SendBotHelp(title="Bot Commands", description="Here are all the commands available:")
        embed.mapping = mapping
        channel = self.get_destination()
        await channel.send(embed=embed.get())
    
    """
    Sends help information for a specific cog.

    This method generates and sends an embed containing details about the commands 
    within a given cog.

    Command: help `NameCog`
    """
    async def send_cog_help(self, cog: Cog):
        embed = SendCogHelp(title=f"{cog.qualified_name} Commands", description=cog.description)
        embed.set({"cog":cog})
        channel = self.get_destination()
        await channel.send(embed=embed.get())
    
    """
    Sends help information for a specific command group.

    Command: help `group-cog`
    """
    async def send_group_help(self, group: Group):
        embed = SendGroupHelp(title=f"{group.name} Group Commands", description=group.help)
        embed.set({"group": group})
        channel = self.get_destination()
        await channel.send(embed=embed.get())
    
        """
    Sends detailed help information for a specific command.

    Command: help `command-name`
    """
    async def send_command_help(self, command: Command):
        embed = SendCommandHelp(title=f"Command name: {command.name}", description=command.help)
        embed.command = command
        embed.help = self
        
        channel = self.get_destination()
        await channel.send(embed=embed.get())

