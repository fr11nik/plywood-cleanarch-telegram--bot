from dataclasses import dataclass,field
from datetime import datetime
from .organization import Organization
from .order import Order
from .user_position import Position

 
@dataclass
class User:
    id: int 
    firstname: str
    lastname: str
    phone_number: str = field(default_factory='')
    birth_date: datetime = field(default=datetime.now()) 
    position: Position = field(default_factory=None) 
    organization: Organization = field(default_factory=None) 
    email:str = field(default_factory='') 
    orders:list[Order] = field(default_factory=list)
    
