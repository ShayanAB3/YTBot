from discord.ext import commands 

class Cogs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot