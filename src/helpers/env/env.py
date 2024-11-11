import os
from dotenv import load_dotenv

load_dotenv()

class Env:
    def readEnv(attr:str):
        return os.getenv(attr)