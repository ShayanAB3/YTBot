from discord.ext.commands.context import Context
from middleware.middleware import Middleware

class FirstMiddleware(Middleware):
    async def handler(self,command: Context) -> bool | None:
        await command.send("Middleware working")
        

    async def failed_handler(self, command: Context):
        await command.send("У вас нет прав для выполнения этой команды.")