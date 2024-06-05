from domain.entity.user import User
from dataclasses import dataclass
from config import DatabaseConfig 
from domain.entity.user_identification import UserIdentification 
from domain.entity.user_position import Position 
import psycopg2
import atexit
from typing import Optional


@dataclass
class Repository:
    """postgres database"""

    def __init__(self,cfg:DatabaseConfig):

        atexit.register(self.exit_handler)
        conn = psycopg2.connect(database=cfg.database,
                        host=cfg.host,
                        user=cfg.user,
                        password=cfg.password,
                        port=cfg.port)
        self.cursor = conn.cursor()
        self.conn = conn

    def exit_handler(self):
       self.cursor.close() 
       print("database connection closed!")
    
    def get_user_identification(self,code:str) -> Optional[UserIdentification]:
        try:
            query = """
            SELECT ui.code, p.id, p.name
            FROM user_identification ui
            INNER JOIN positions p ON p.id = ui.position_id
            WHERE ui.code = %s;
            """
            self.cursor.execute(query, [code])
            row = self.cursor.fetchone()
            if row:
                code, position_id, position_name = row
                position = Position(id=position_id, name=position_name)
                user_identification = UserIdentification(code=code, position=position)
                return user_identification
            else:
                return None
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return None

       
    def get_user_by_id(self,id:id) -> Optional["User"]:
        try:
            query = """
            SELECT id,firstname,lastname,phone_number FROM users WHERE id = %s LIMIT 1;
            """
            self.cursor.execute(query, (id,))
            row = self.cursor.fetchone()
            if row:
                id,firstname,lastname,phone_number= row
                usr = User(id=id, firstname=firstname, lastname=lastname,phone_number=phone_number)
                return usr  
            else:
                return None
        except psycopg2.Error as e:
            print(f"Database error: {e}")
            return None

    def create_user(self,usr:User):
        try:
            query = """
            INSERT INTO users(
            id, firstname, lastname, phone_number, position_id,birth_date)
            VALUES (%(id)s, %(firstname)s, %(lastname)s, %(phone_number)s, %(position_id)s,%(birth_date)s);
            """
            self.cursor.execute(query, 
            {'id':usr.id,'firstname':usr.firstname,
             'lastname':usr.lastname,'phone_number':usr.phone_number,
             'position_id':usr.position.id,'birth_date':usr.birth_date})
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Database error: {e}")