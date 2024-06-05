from dataclasses import dataclass,field
from datetime import datetime
from .order import Order
from .user_position import Position
from typing import Optional

@dataclass
class User:
    id: int
    firstname: str
    lastname: str
    phone_number: str = ''
    birth_date: datetime = field(default_factory=datetime.now)
    position: Optional['Position'] = None
    organization: str = ''
    email: str = ''
    orders: list['Order'] = field(default_factory=list)
    
