from dataclasses import dataclass,field

@dataclass
class SupportChat:
    user_id: int
    problem_description: str
    response: str = field(default_factory=str)
