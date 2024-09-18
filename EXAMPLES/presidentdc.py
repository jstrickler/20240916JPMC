from dataclasses import dataclass

@dataclass
class President:
    term: int
    first_name: str
    last_name: str
    birth_place: str
    birth_state: str
    party: str