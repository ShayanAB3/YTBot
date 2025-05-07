from sqlalchemy import create_engine, Engine
from public.orm.config import Config

class SQLEngine:
    config:Config = Config()
    engine:Engine
    
    def __init__(self):
        self.engine = create_engine(self.config.get_config_mysql())
    
    def get_engine(self) -> Engine:
        return self.engine