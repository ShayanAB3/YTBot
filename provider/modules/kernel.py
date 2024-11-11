from provider.modules.provider.cogs_provider import CogsProvider
from provider.modules.provider.command_provider import CommandProvider
from provider.modules.provider.event_provider import EventProvider

from src.provider.module import Module

class Kernel:
    modules:list[Module] = [CogsProvider,CommandProvider,EventProvider]
    def get_module(self,module:Module):
        module_class:Module = module()
        modules = module_class.get_modules()
        return modules

    def get_modules(self) -> list[str]:
        list_modules = list(map(self.get_module, self.modules))
        return [item for sublist in list_modules for item in sublist]

kernel = Kernel()