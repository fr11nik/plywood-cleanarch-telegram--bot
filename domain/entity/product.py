from dataclasses import dataclass
from datetime import datetime

@dataclass
class Product:
    id: int
    name: str
    type: str
    color: str
    shape: str
    application: str
    treatment: str
    price: float
    min_ready_date: datetime

