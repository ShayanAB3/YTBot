from src.command_error.command.command import Command
from error.kernel import kernel

class CommandContext(Command):
    async def send(self, message:str,**kwargs):
        await self.command.send(message,**kwargs)
    
    async def execute_not_found_exceptions(self, error:Exception):
        await kernel.not_found_exceptions_context(self.command,error)