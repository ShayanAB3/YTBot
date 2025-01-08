from middleware.middleware import Middleware
from discord.ext.commands.context import Context
from src.exception.stop_exception import StopException


class CmdKernel:
    cmd:dict[str,str] = {}
    middleware:dict[str,Middleware] = {}
    
    def set_cmd_middleware(self,command:str,middleware:str):
        self.check_middleware(middleware)
        if self.is_not_dublicate(command):
            self.cmd[command] = middleware

    def check_middleware(self,middleware:str,callback:callable=None):
        if not self.middleware.get(middleware):
           raise Exception("Middleware is not registered") if callback == None else callback()

    def is_not_dublicate(self,command:str) -> bool:
        return self.cmd.get(command) == None


    async def active_middleware(self,command:Context):
        command_name:str = command.command.name
        middleware_key = self.cmd.get(command_name)
        if not middleware_key:
            return
        middleware:Middleware = self.middleware[middleware_key]()
        if await middleware.handler(command) == False:
            await middleware.failed_handler(command)
            raise StopException
            