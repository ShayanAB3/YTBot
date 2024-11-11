from discord.ext import commands
from route.command.command import Command

from route.facade.access import Access
from route.facade.permission import Permission
from route.facade.channel import Channel
from route.facade.middleware import Middleware

from typing import Union

class Prefix(Command,Middleware,Access,Permission,Channel):
    def command(self,name:str,*,description:str="",middleware:str="",channel:Union[str,int]=""):
        self.set_args(name,middleware,channel) 
        return commands.command(name=name,description=description,help="Command helping for yours")
    
    def set_args(self,name:str,middleware:str,channel_name:str):
        self.name = name
        self.set_middleware(middleware)
        self.channel_only(channel_name)

    def group(self,name):
        return commands.group(name)

    def is_owner(self):
        return commands.is_owner()