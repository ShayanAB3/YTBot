from provider.storage.storage_provider import StorageProvider
from pathlib import Path
from discord import File

class Storage:
    storage_dir:str = StorageProvider.dirname
    path_lib:Path
    path_name:str

    def __init__(self, dirname:str):
        self.path_name = f"./{self.storage_dir}/{dirname}"
        self.path_lib = Path(self.path_name)
        if not self.path_lib.is_dir():
            self.path_lib.mkdir()
    
    def get(self,file_name:str) -> File:
        return File(f"{self.path_name}/{file_name}", filename=file_name)

    def upload(self,file:bytes,path:str):
        with open(f"{self.path_name}/{path}", 'wb') as f:
                f.write(file)
        