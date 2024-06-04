from dataclasses import dataclass,field
from user import User
from order import Order
from product import Product

@dataclass
class User_Orders:
    order: Order
    user: User
    products: list[Product] = field(default_factory=list)

