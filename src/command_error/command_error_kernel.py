from discord.ext.commands import Context, CommandInvokeError
from error.command_error_handler import CommandErrorHandler
from abc import ABC, abstractmethod

class CommandErrorKernel(ABC):
    exceptions:dict[Exception,str | CommandErrorHandler] = {}

    @abstractmethod
    async def not_found_exceptions(self, ctx:Context, error:Exception):
        pass

    def get_exception(self,exception:CommandInvokeError):
        error = exception.original if isinstance(exception, CommandInvokeError) else exception
        for exception_key in self.exceptions.keys():
            if isinstance(error,exception_key):
                return self.exceptions.get(exception_key)

    async def active_command_error(self,context: Context, exception: Exception):
        exception_value:CommandErrorHandler | str | None = self.get_exception(exception)

        if not exception_value:
            return await self.not_found_exceptions(context,exception)
        
        if isinstance(exception_value,CommandErrorHandler):
            return await exception_value.handler(context,exception)
        
        if isinstance(exception_value,str):
            return await context.send(exception_value)