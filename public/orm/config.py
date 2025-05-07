from src.helpers.env.env import Env

class Config:
    DB_HOST=Env.readEnv("DB_HOST")
    DB_PORT=Env.readEnv("DB_PORT")
    DB_NAME=Env.readEnv("DB_NAME")
    DB_USER=Env.readEnv("DB_USER")
    DB_PASS=Env.readEnv("DB_PASS")

    def get_config_mysql(self) -> str:
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    