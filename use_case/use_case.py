from domain.entity.entities import Message
from domain.entity.user import User
from domain.entity.user_identification import UserIdentification
from .interfaces import PostgresRepo
from typing import Optional

class UseCase:
    def init(self,pgRepo:PostgresRepo):
        self.pgRepo = pgRepo

    def get_welcome_message(self):
        return Message("Здравствуйте! Вас приветствует бот-помощник компании “Новаторы прогресса” \n Пожалуйста, выберите один из пунктов чтобы продолжить")

    def auth_user(self,u:User):
        u = self.pgRepo.get_user(u.id)
        print(u)
        return u.firstname == "Ivan" 
    
    def get_user_identification(self,code:str) -> UserIdentification:
        return self.pgRepo.get_user_identification(code=code)

    def get_user_by_id(self,id:id) -> Optional[User]:
        return self.pgRepo.get_user_by_id(id)

    def create_user(self,usr:User):
        self.pgRepo.create_user(usr) 


