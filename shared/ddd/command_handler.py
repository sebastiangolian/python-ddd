from abc import abstractmethod
from typing import List

from shared.services.validation_service import ValidationService


class CommandHandler:
    @abstractmethod
    async def handle(self) -> None:
        pass

    @property
    def validators(self) -> List[tuple]:
        return []

    def validate(self) -> None:
        ValidationService(self.validators).validate()
