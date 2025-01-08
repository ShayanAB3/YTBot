from discord.ext.commands import Context, CommandInvokeError
from discord import Interaction
from error.command_error_handler import CommandErrorHandler
from abc import ABC, abstractmethod
from typing_extensions import Union
from src.command_error.command.command import Command

class CommandErrorKernel(ABC):
    exceptions:dict[Exception,Union[str, CommandErrorHandler]] = {}

    @abstractmethod
    async def not_found_exceptions_context(self, ctx:Context, error:Exception):
        pass

    @abstractmethod
    async def not_found_exceptions_interaction(self, ctx:Interaction, error:Exception):
        pass


    def get_exception(self,exception:CommandInvokeError):
        error = exception.original if isinstance(exception, CommandInvokeError) else exception
        for exception_key in self.exceptions.keys():
            if isinstance(error,exception_key):
                return self.exceptions.get(exception_key)

    async def active_command_error(self,command:Command, exception: Exception):
        exception_value:Union[CommandErrorHandler,str,None] = self.get_exception(exception)

        if not exception_value:
            await command.execute_not_found_exceptions(exception)
            return
        
        if isinstance(exception_value,CommandErrorHandler):
            return await exception_value.handler(command,exception)
        
        if isinstance(exception_value,str):
            return await command.send(exception_value)