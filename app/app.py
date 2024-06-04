from handler.telegram_bot.bot import Bot 
from handler.telegram_bot.v1.handler import V1Handler
from use_case.use_case import UseCase
from .container import Container
from dataclasses import dataclass
from config import Config

@dataclass
class App:
    """Initial app that used for start any dependecy such tg_bot http grpc etc.."""

    def __init__(self,config_path:str):
        cfg = Config(config_path)
        self.cfg = cfg
    
    def StartTelegramBot(self):
        ##init bot
        bot = Bot(self.cfg.tg_config.secret)    

        ##create handler and inject use_case
        v1 = V1Handler()
        self.container = Container()
        uc = self.container.GetUseCase(self.cfg)
        v1.init(uc)

        ##inject handler to bot
        bot.WithHandler(v1)
        bot.Run()


