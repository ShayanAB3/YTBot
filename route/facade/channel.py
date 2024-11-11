from channel.kernel import kernel
from route.facade.facade import decorator

class Channel:
    name:str
    def channel_only(self,channel_name:str):
        kernel.set_list_channel(channel_name,self.name)
        return decorator

    def channel_only_id(self,channel_id:int):
        kernel.set_list_channel(channel_id,self.name)
        return decorator