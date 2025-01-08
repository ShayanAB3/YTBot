from discord.ext.commands import Context, ChannelNotFound
from error.command_error_handler import CommandErrorHandler

class ChannelNotFoundHandler(CommandErrorHandler):
    async def handler(self,command: Context, error: ChannelNotFound):
        await command.send(f"Канал {error.argument} не найдена")