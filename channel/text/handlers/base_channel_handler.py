from discord.ext.commands import Context
from channel.text.channel_handler import ChannelHandler

class BaseChannelHandler(ChannelHandler):
    async def handler(self, ctx: Context):
        await ctx.send("Вы должны использовать комманду в канале 'основной'")