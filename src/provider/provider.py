class Provider:
    dirname:str = ""
    endswith:str = ""
    remove_paths:list[str] = []
    remove_modules:list[str] = []

    def __init__(self):
        self.set_dirname_removes(self.remove_paths)

    def set_dirname_removes(self,removes:list[str]):
        if removes:
            for index, path in enumerate(removes):
                removes[index] = f"{self.dirname}/{path}"