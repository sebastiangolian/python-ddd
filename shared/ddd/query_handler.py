from abc import abstractmethod
from dataclasses import dataclass
from typing import List

from shared.services.validation_service import ValidationService


@dataclass
class PaginationQuery:
    limit: int = 500
    page: int = 1


class QueryHandler:
    @abstractmethod
    def get(self) -> None:
        pass

    @property
    def validators(self) -> List[tuple]:
        return []

    def validate(self) -> None:
        ValidationService(self.validators).validate()
