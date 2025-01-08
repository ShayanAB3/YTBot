from src.helpers.env.env import Env

class StorageProvider:
    dirname:str = Env.readEnv("STORAGE_DIR")
