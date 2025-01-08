from discord.ext.commands.context import Context
from discord.ext.commands import CommandError
from discord import Interaction

from access.check_failure_handler import CheckFailureHandler
from typing_extensions import Union

class AccessKernel:
    cmd:dict[str,str] = {}
    permissions:dict[str,CheckFailureHandler] = {}
    roles:dict[str,CheckFailureHandler] = {}

    def get_roles_and_permissions(self) -> dict[str,CheckFailureHandler]:
        return self.roles | self.permissions

    def set_cmd_access(self, command:str, role:str):
        roles_and_permissions = self.get_roles_and_permissions()
        self.check_access(role,roles_and_permissions)
        if self.is_not_dublicate(command,roles_and_permissions):
            self.cmd[command] = role

    def get_access_handler(self,access_key:str) -> CheckFailureHandler:
        check_failure:CheckFailureHandler = self.get_roles_and_permissions().get(access_key)()
        return check_failure

    def is_not_dublicate(self,command:str,access_list:dict[str,CheckFailureHandler]) -> bool:
        return access_list.get(command) == None

    def check_access(self,access_key:str,access_list:dict[str,CheckFailureHandler] ,callback:callable=None):
       if not access_list.get(access_key):
          raise Exception(f"Key {access_key} not exists") if callback == None else callback()

    async def active_access(self,context: Union[Context,Interaction], exception:CommandError) -> bool | None:
        command_name:str = str(context.command)
        access_key = self.cmd.get(command_name)
        if not access_key:
            return False
        handler:CheckFailureHandler = self.get_access_handler(access_key)
        await handler.handler(context,exception)