from src.provider.module import Module

class CogsProvider(Module):
    dirname:str = "cogs"
    endswith:str = ".py"
    remove_paths:list[str] = []
    remove_modules:list[str] = ['cogs.cogs','cogs.group.group']