import discord
from discord.ext import commands
from discord.ext.commands.context import Context

from middleware.kernel import kernel as kernel_middleware
from access.kernel import kernel as kernel_access
from provider.modules.kernel import kernel as kernel_provider
from channel.kernel import kernel as kernel_channel
from error.kernel import kernel as kernel_command_error

from src.globals.context import context as global_context

from facade.bot.bot import bot as global_bot


from src.helpers.env.env import Env
from src.exception.stop_exception import StopException

from src.command_error.command.command_context import CommandContext
from src.command_error.command.command_interaction import CommandInteraction

import discord
import logging

from help.help import Help

intents = discord.Intents.all()
intents.message_content = True
intents.voice_states = True
intents.members = True

command_prefix = Env.readEnv("COMMAND_PREFIX")
token = Env.readEnv("TOKEN")

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=command_prefix,intents=intents)
        self.before_invoke(self.before_any_command)

    async def on_ready(self):
        self.loop.create_task(self.tree.sync())
        discord.utils.setup_logging()
        logger = logging.getLogger(__name__)
        logger.info(f'Logged in as {self.user}')

    async def setup_hook(self):
        modules_list = kernel_provider.get_modules()
        for ext in modules_list:
            await self.load_extension(ext)

    async def on_command_error(self, context: Context, exception: Exception):
        if isinstance(exception,StopException):
            return
        is_found_access = await kernel_access.active_access(context,exception)
        if is_found_access == False:
            command = CommandContext(context)
            await kernel_command_error.active_command_error(command,exception)

    async def before_any_command(self, context:Context):
        global_context.set(context)
        await kernel_channel.check_access_channel(context)
        await kernel_middleware.active_middleware(context)
    
client = Client()
client.help_command = Help()


global_bot.set(client)

if __name__ == "__main__":
    client.run(token)