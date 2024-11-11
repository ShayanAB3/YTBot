from src.command_error.command_error_kernel import CommandErrorKernel
from error.command_error_handler import CommandErrorHandler

#Import key exceptions
from discord.ext.commands import Context, MissingAnyRole , MemberNotFound, ChannelNotFound, CommandNotFound
from aiohttp import ClientResponseError
from error.handlers.channel_not_found_handler import ChannelNotFoundHandler
from error.handlers.command_not_found_handler import CommandNotFoundHandler

class Kernel(CommandErrorKernel):
    exceptions:dict[Exception,str | CommandErrorHandler] = {
        MemberNotFound: "Members not found",
        MissingAnyRole: "Missing roles",
        ClientResponseError: "Command ClientResponseError error",
        ChannelNotFound: ChannelNotFoundHandler(),
        CommandNotFound: CommandNotFoundHandler()
    }

    async def not_found_exceptions(self, ctx:Context, error:Exception):
        await ctx.send(error.__str__())

kernel = Kernel()