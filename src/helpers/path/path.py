from pathlib import Path as PathLib
from os.path import exists
from src.helpers.logging.logging import Logging


class Path(PathLib):
    listdir:list[PathLib] = []     
    exclude_dirs:list[str] = ["__pycache__"]

    def set_path(self,path:PathLib):
        self.path = path

    def is_exists(self) -> bool:
        return exists(self.path)

    def read(self,besides:list[str] = [], endswith:str = ".py") -> list[PathLib]:
        exclude_dirs = {str(self / d) for d in self.exclude_dirs}
        dirs = []
        search_prefix = f"*{endswith}"
        for file in self.rglob(search_prefix):
             # Проверяем, находится ли файл в исключённой папке
             if not any(str(file).startswith(ex_dir) for ex_dir in exclude_dirs):
                 dirs.append(file)

        self.listdir = dirs
        if besides:
            return self.remove(besides)
        
        return self.listdir

    def remove(self,listdir:list[str]) -> list[str]:
        for dir in listdir:
            path_dir = PathLib(dir)
            if path_dir not in self.listdir:
                Logging.error(f"Path {path_dir} not exists")
                continue
            self.listdir.remove(path_dir)
        return self.listdir

    def convert_path_to_module(self) -> str:
        if not self.path:
            return Logging.error("Path is empty")
        if not self.is_exists():
            return Logging.error(f"Path {self.path} not exists")
        return self.path.with_suffix('').as_posix().replace('/', '.')