from access.kernel import kernel as kernel_access
from src.reason.role import Role
from discord.ext import commands

class Access:
    name:str
    def set_access_role(self,role:str):
       if role and self.name:
            kernel_access.set_cmd_access(self.name,role)
            handler_failure = kernel_access.get_access_handler(role)
            role:Role = handler_failure.reason().get()
            if role:
                return commands.has_any_role(*role)