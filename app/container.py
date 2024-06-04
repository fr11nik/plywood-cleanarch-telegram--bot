from adapter import PostgresRepo as RealPostgresRepo
from use_case.interfaces import UseCase,PostgresRepo
from use_case.use_case import UseCase as RealUC
from config import Config,DatabaseConfig

class Container:
    def GetUseCase(self,cfg:Config) -> UseCase:
        uc = RealUC() 
        uc.init(self.GetPostgresRepo(cfg.db_config))
        return uc

    def GetPostgresRepo(self,cfg:DatabaseConfig) -> PostgresRepo:
        return RealPostgresRepo(cfg=cfg)
    