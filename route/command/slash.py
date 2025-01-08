from discord import app_commands
from route.command.command import Command

class Slash(Command):
    def command(self,name:str,description:str):
        return app_commands.command(name=name,description=description)

    def describe(self,**kwargs):
        return app_commands.describe(**kwargs)
