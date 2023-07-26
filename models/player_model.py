from dataclasses import dataclass


@dataclass
class PlayerModel:
    id: int
    first_name: str
    last_name: str
    full_name: str
    is_active: bool
