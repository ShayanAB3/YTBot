from discord import app_commands
from route.command.command import Command
from route.facade.middleware import Middleware

class Slash(Command,Middleware):
    def command(self,name:str,description:str,*,middleware:str=""):
        self.set_args(name,middleware)
        return app_commands.command(name=name,description=description)
    
    def set_args(self,name:str,middleware:str):
        self.name = name
        self.set_middleware(middleware)

    def describe(self,**kwargs):
        return app_commands.describe(**kwargs)
