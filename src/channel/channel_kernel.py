from discord import utils
from src.exception.stop_exception import StopException
from discord.ext.commands import Context, ChannelNotFound
from typing import Union

from facade.bot.bot import bot

from channel.text.channel_handler import ChannelHandler
from discord.abc import PrivateChannel, GuildChannel
from discord import Thread


class ChannelKernel:
    list_channel:dict[str,str | int] = {}
    channels_not_access_handler:dict[str | int ,str | ChannelHandler] = {}

    def set_list_channel(self,name: Union[str,int],command_name: str):
        if name and command_name:
            self.list_channel[command_name] = name

    
    def get_name_channel(self,ctx: Context,name: str) -> GuildChannel:
        channel = utils.get(ctx.guild.channels,name=name)
        return self.check_channel(channel,name)

    def get_id_channel(self, id:int) -> GuildChannel:
        channel = bot.get().get_channel(id)
        return self.check_channel(channel,id)
    
    def get_channel(self,ctx:Context) -> GuildChannel:
        channel_name_or_id:Union[str,int] = self.list_channel.get(ctx.command.name)
        if isinstance(channel_name_or_id,int):
            return self.get_id_channel(channel_name_or_id)
        return self.get_name_channel(ctx,channel_name_or_id)


    async def check_access_channel(self,ctx:Context):
        if self.is_ignore_channels(ctx):
            return
        channel = self.get_channel(ctx)
        if channel.id != ctx.channel.id:
            await self.active_channels_not_access_handler(ctx,channel)
            raise StopException
        
    def check_channel(self,channel,name_or_id:Union[str,int]):
        if not channel:
            raise ChannelNotFound(name_or_id)
        return channel
    

    def is_ignore_channels(self,ctx: Context) -> bool:
        #Command that are not registered
        if not self.list_channel.get(ctx.command.name):
            return True
        if isinstance(ctx.message.channel,PrivateChannel):
            raise StopException
        if isinstance(ctx.message.channel,Thread):
            raise StopException
        return False


    async def active_channels_not_access_handler(self,ctx: Context,channel: GuildChannel):
        handler: str | ChannelHandler = self.channels_not_access_handler.get(channel.name) or self.channels_not_access_handler.get(channel.id)
        if isinstance(handler,str):
            return await ctx.send(handler)
        if isinstance(handler,ChannelHandler):
            return await handler.handler(ctx)
        