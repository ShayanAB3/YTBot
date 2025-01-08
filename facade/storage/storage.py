from provider.storage.storage_provider import StorageProvider
from pathlib import Path
from discord import File as DiscordFile
from io import TextIOWrapper

class Storage:
    """
    A class for managing file storage within a specified directory.

    Attributes:
        storage_dir (str): The base directory for storage, sourced from StorageProvider.
        path_lib (Path): The Path object representing the full directory path.
        path_name (str): The string representation of the directory path.
    """
    storage_dir: str = StorageProvider.dirname
    path_lib: Path
    path_name: str

    def __init__(self, dirname: str):
        """
        Initializes the Storage instance and ensures the specified directory exists.

        :param dirname: The name of the subdirectory to manage.
        :type dirname: str
        """
        self.path_name = f"./{self.storage_dir}/{dirname}"
        self.path_lib = Path(self.path_name)
        if not self.path_lib.is_dir():
            self.path_lib.mkdir()

    def get(self,file_name:str) -> DiscordFile:
        """
        Retrieves a file as a `discord.File` object from the specified path.

        :param file_name: The name of the file to retrieve.
        :type file_name: str
        :return: A `discord.File` object representing the specified file.
        :rtype: discord.File
        """
        return DiscordFile(f"{self.path_name}/{file_name}", filename=file_name)

    def get_file(self,file_name:str) -> TextIOWrapper:
        """
        Opens a file in read and write mode ('r+') located at the path defined in the instance.

        :param file_name: The name of the file to be opened.
        :return: TextIOWrapper: The file object that can be used to read from and write to the file.
        Raises:
            FileNotFoundError: If the file specified by `file_name` does not exist in the specified path.
            IOError: If an error occurs while opening or reading the file, such as insufficient permissions or file corruption.
        """
        return open(f"{self.path_name}/{file_name}", "r+",encoding="utf-8")

    def upload(self, file: bytes, path: str):
        """
        Uploads a file to the specified path within the object's directory.

        :param file: The binary content of the file to upload.
        :type file: bytes
        :param path: The relative path where the file will be saved.
        :type path: str
        """
        with open(f"{self.path_name}/{path}", 'wb') as f:
            f.write(file)
        