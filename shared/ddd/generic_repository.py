from abc import ABC, abstractmethod
from typing import Any, List, Optional

from infrastructure.db.db_interface import DbInterface
from shared.ddd.entity import Entity


class GenericRepository(ABC):
    @abstractmethod
    def __init__(self, db: DbInterface) -> None:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def get(self, limit: Optional[int] = None, page: Optional[int] = None) -> List[Entity]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Entity:
        pass

    @abstractmethod
    def get_by_ids(self, ids: List[int]) -> Entity:
        pass

    @abstractmethod
    def remove(self, id: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def save(self, entity: Entity) -> None:
        pass

    @abstractmethod
    def find_by_attribute(self, attibute: str, value: Any) -> List[Entity]:
        pass
