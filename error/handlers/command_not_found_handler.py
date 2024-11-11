from discord.ext.commands import Context, CommandNotFound 
from error.command_error_handler import CommandErrorHandler

class CommandNotFoundHandler(CommandErrorHandler):
    async def handler(self, ctx: Context, error: CommandNotFound):
        command_name = str(error).split('"')[1]
        await ctx.send(f"Команда '{command_name}' не найдена.")