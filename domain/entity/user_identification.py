from dataclasses import dataclass,field
from .user_position import Position


@dataclass
class UserIdentification:
    code: str = "" 
    position: Position = field(default_factory=Position(id=-1,name=''))

    def __repr__(self):
        return f"UserIdentification(code={self.code}, position={self.position})"