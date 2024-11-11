from src.provider.provider import Provider
from src.provider.module import Module

class CommandProvider(Module):
    dirname:str = "command"
    endsWithName:str = ".py"
    remove_paths:list[str] = []
    remove_modules:list[str] = []