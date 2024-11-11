from discord.ext import commands 
from discord.ext.commands.context import Context
from discord.ext.commands.errors import CommandError
from discord import Message, Member, User, Reaction, Guild

class Event(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_message(self, message:Message):
        pass

    
    @commands.Cog.listener()
    async def on_member_join(self, member:Member):
        pass

    
    @commands.Cog.listener()
    async def on_member_remove(self, member:Member):
        pass

    
    @commands.Cog.listener()
    async def on_ready(self):
        pass

    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction:Reaction, user:User):
        pass

    
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction:Reaction, user:User):
        pass

    
    @commands.Cog.listener()
    async def on_guild_join(self, guild:Guild):
        pass

    
    @commands.Cog.listener()
    async def on_error(self, event:str, *args, **kwargs):
        pass
    
     
    @commands.Cog.listener()
    async def on_command_error(self, context: Context, exception: CommandError):
        pass
