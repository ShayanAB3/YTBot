from src.provider.module import Module

class EventProvider(Module):
    dirname:str = "event"
    endsWithName:str = ".py"
    remove_paths:list[str] = []
    remove_modules:list[str] = []