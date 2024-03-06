from abc import abstractmethod
from typing import Any, List

from domain.entity.student import Student
from shared.ddd.generic_repository import GenericRepository


class StudentRepositoryInterface(GenericRepository):
    @abstractmethod
    def get_by_id(self, id: int) -> Student:
        pass

    @abstractmethod
    def find_by_attribute(self, attibute: str, value: Any) -> List[Student]:
        pass
