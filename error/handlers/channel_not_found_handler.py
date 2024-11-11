from discord.ext.commands import Context, ChannelNotFound
from error.command_error_handler import CommandErrorHandler

class ChannelNotFoundHandler(CommandErrorHandler):
    async def handler(self,ctx: Context, error: ChannelNotFound):
        await ctx.send(f"Канал {error.argument} не найдена")