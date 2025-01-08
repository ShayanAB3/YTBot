from src.command_error.command_error_kernel import CommandErrorKernel
from error.command_error_handler import CommandErrorHandler
from discord import Interaction
from discord.ext.commands import Context

#Import key exceptions
from discord.ext.commands import MissingAnyRole , MemberNotFound, ChannelNotFound, CommandNotFound
from aiohttp import ClientResponseError
from error.handlers.channel_not_found_handler import ChannelNotFoundHandler
from error.handlers.command_not_found_handler import CommandNotFoundHandler

from typing_extensions import Union

class Kernel(CommandErrorKernel):
    exceptions:dict[Exception,Union[str, CommandErrorHandler]] = {
        MemberNotFound: "Members not found",
        MissingAnyRole: "Missing roles",
        ClientResponseError: "Command ClientResponseError error",
        ChannelNotFound: ChannelNotFoundHandler(),
        CommandNotFound: CommandNotFoundHandler()
    }

    async def not_found_exceptions_context(self, ctx:Context, error:Exception):
        await ctx.send(error.__str__())
    
    async def not_found_exceptions_interaction(self, interaction:Interaction, error:Exception):
        await interaction.response.send_message(error.__str__())

kernel = Kernel()