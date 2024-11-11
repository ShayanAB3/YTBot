from access.kernel import kernel as kernel_access
from discord.ext import commands


class Permission:
    name:str
    def set_access_permission(self,permission:str):
        if permission and self.name:
            kernel_access.set_cmd_access(self.name,permission)
            handler_failure = kernel_access.get_access_handler(permission)
            permission:Permission = handler_failure.reason().get()
            if permission:
                return commands.has_permissions(**permission)