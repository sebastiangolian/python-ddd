from abc import ABC, abstractmethod
from typing import Any, List, Optional


class DbInterface(ABC):
    @abstractmethod
    def set_resource(self, resource: str) -> "DbInterface":
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def get(self, limit: Optional[int] = None, page: Optional[int] = None) -> List[object]:
        pass

    @abstractmethod
    def get_all_items(self) -> str:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> object:
        pass

    @abstractmethod
    def get_by_ids(self, id: int) -> object:
        pass

    @abstractmethod
    def get_by_attribute(self, attribute: str, value: Any) -> List[object]:
        pass

    @abstractmethod
    def add(self, item: Any) -> None:
        pass

    @abstractmethod
    def update(self, id: int, item: Any) -> None:
        pass

    @abstractmethod
    def remove(self, id: int) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
