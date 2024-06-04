from abc import ABC, abstractmethod
from domain.entity.user import User 
from domain.entity.user_identification import UserIdentification
from typing import Optional

class PostgresRepo(ABC):
    @abstractmethod
    def get_user_identification(self,code:str) -> Optional["UserIdentification"]:
        pass

    @abstractmethod
    def get_user_by_id(self,id:id) -> Optional["User"]:
        pass

class UseCase(ABC):
    @abstractmethod
    def init(self,pgRepo:PostgresRepo):
        pass

    @abstractmethod
    def get_welcome_message(self):
        pass

    @abstractmethod
    def auth_user(self,u:User) -> bool:
        pass

    @abstractmethod
    def get_user_identification(self,code:str) -> Optional["UserIdentification"]:
        pass
   
    @abstractmethod
    def get_user_by_id(self,id:id) -> Optional["User"]:
        pass
