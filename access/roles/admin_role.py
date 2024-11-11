from discord.ext.commands import CommandError, Context
from src.reason.reason import Reason
from src.access.role import Role

class AdminRole(Role):
    def reason(self) -> Reason:
        self.role.set_permission_role("Admins")
        return self.role

    async def handler(self, ctx: Context, error: CommandError):
        await ctx.send("Доступно только для админов")