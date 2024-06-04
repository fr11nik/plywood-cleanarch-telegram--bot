from dataclasses import dataclass

@dataclass
class Position:
    id: int 
    name: str 
    def __repr__(self):
        return f"Position(id='{self.id}', name='{self.name}')"
