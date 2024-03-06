import uuid
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Entity:
    id: str = None

    def __post_init__(self):
        if self.id is None:
            self.id = self.generate_id()

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

    def to_dict(self) -> Dict:
        return self.__dict__

    @staticmethod
    def generate_id() -> str:
        return str(uuid.uuid4())
