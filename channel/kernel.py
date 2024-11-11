from src.channel.channel_kernel import ChannelKernel

from channel.text.channel_handler import ChannelHandler as ChannelHandlerText

#Handler text
from channel.text.handlers.base_channel_handler import BaseChannelHandler

class Kernel(ChannelKernel):
    """dict[channel_name | channel_id: str | ClassHandler]"""
    channels_not_access_handler:dict[str | int ,str | ChannelHandlerText] = {
        749932484241653773: BaseChannelHandler()
    }

kernel = Kernel()