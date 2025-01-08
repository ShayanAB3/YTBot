from functools import partial
from discord.ui import Button, View
from typing_extensions import Any
from discord import Interaction
from facade.bot.bot import bot as global_bot


class Paginate:
    nums_pages:list[int] = []
    
    command:str
    group:str
    args:dict[str,Any] = {}

    def __init__(self,count:int):
        self.count = count

    async def paginate_page(self,interaction:Interaction,page:int):
        bot = global_bot.get()
        self.args.update({"page":page})

        if self.command and self.group:
            group = bot.tree.get_command(self.group)
            subcommand = group.get_command(self.command)
            await subcommand.callback(group,interaction, **self.args)
            return
        if self.command:
            command = bot.tree.get_command(self.command)
            await command.callback(self, interaction, **self.args)
            return

    def generate(self,view:View):
        if not self.count >= 1:
            return
        for page in range(1,self.count+1):
            button = Button(label=f"{page}")
            button.callback = partial(self.paginate_page, page=page)
            view.add_item(button)