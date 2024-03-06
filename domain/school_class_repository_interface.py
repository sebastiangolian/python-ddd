from abc import abstractmethod
from typing import Any, List

from domain.entity.school_class import SchoolClass
from shared.ddd.generic_repository import GenericRepository


class SchoolClassRepositoryInterface(GenericRepository):
    @abstractmethod
    def get_by_id(self, id: int) -> SchoolClass:
        pass

    @abstractmethod
    def find_by_attribute(self, attibute: str, value: Any) -> List[SchoolClass]:
        pass
