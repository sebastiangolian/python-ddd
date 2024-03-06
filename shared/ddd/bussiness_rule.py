from abc import ABC, abstractmethod


class BusinessRule(ABC):
    @abstractmethod
    def validate(self) -> None:
        pass
