from enum import Enum

from shared.ddd.value_object import ValueObject


class StudentStatus(ValueObject, str, Enum):
    NEW = "NEW"
    REGISTERED = "REGISTERED"
    DELETED = "DELETED"

    @property
    def is_new(self) -> bool:
        return self == StudentStatus.NEW

    @property
    def is_registered(self) -> bool:
        return self == StudentStatus.REGISTERED

    @property
    def is_deleted(self) -> bool:
        return self == StudentStatus.DELETED
