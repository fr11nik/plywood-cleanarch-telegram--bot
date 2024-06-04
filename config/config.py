import yaml
from dataclasses import dataclass,field

@dataclass
class TelegramConfig:
    secret: str

@dataclass
class DatabaseConfig:
    database: str = "postgres"
    host: str = "localhost"
    user: str = "postgres"
    password: str = "root"
    port: str = "5432"


class Config:
    """Config class that stores yaml files"""
    def __init__(self,filepath:str):

        with open(filepath) as f:
            try:
                config = yaml.safe_load(f)
                self.tg_config = TelegramConfig(secret=config["TELEGRAM_BOT_TOKEN"])
                self.db_config = DatabaseConfig(
                    config["db_config"]["database"],
                    config["db_config"]["host"],
                    config["db_config"]["user"],
                    config["db_config"]["password"],
                    config["db_config"]["port"],
                )
            except yaml.YAMLError as exc:
                print(exc)




