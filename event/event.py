from discord.ext import commands 
from discord import Message
from discord.ext.commands.context import Context
from discord.ext.commands.errors import CommandError
#from discord.ext.commands import CheckFailure

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.Cog.listener()
    async def on_message(self, message:Message):
        print(f'Message from {message.author}: {message.content}')

    @commands.Cog.listener()
    async def on_command_error(self,ctx:Context,error:CommandError):
        pass

async def setup(bot:commands.Bot):
    await bot.add_cog(Event(bot))
