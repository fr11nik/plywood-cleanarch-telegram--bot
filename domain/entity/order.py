from dataclasses import dataclass, field
from datetime import datetime
from .product import Product


@dataclass
class Status:
    id:int
    name:str

@dataclass
class Order:
   id:int
   status: Status
   datetime: datetime
   product_details: list[Product] = field(default_factory=list)

