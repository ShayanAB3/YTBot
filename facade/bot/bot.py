from discord.ext.commands import Bot as DiscordBot

class Bot:
    def set(self,bot: DiscordBot):
        self.bot = bot

    def get(self) -> DiscordBot:
        return self.bot
    
bot = Bot()