from discord.ext.commands import CommandError, Context
from src.access.permission import Permission
from src.reason.reason import Reason

class AdminPermission(Permission):
    def reason(self) -> Reason:
        self.permission.administrator = False
        return self.permission
    
    async def handler(self, ctx: Context, error: CommandError):
        await ctx.send("You not are administrator")