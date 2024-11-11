from src.reason.reason import Reason

class Role(Reason):
    roles:list[str | int] = []
    
    def set_permission_role(self,role:str | int):
        self.roles.append(role)

    def set_permission_roles(self,roles:list[str | int]):
        self.roles = self.roles + roles

    def get(self) -> dict[str | int]:
        return set(self.roles)