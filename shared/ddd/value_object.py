from enum import EnumMeta
from typing import Any, Optional, TypeVar

ValueObjectType = TypeVar("ValueObjectType", bound="ValueObject")


class ValueObject:
    def __composite_values__(self):
        return (self.value,)

    @classmethod
    def from_value(cls, value: Any) -> Optional[ValueObjectType]:
        if isinstance(cls, EnumMeta):
            for item in cls:
                if item.value == value:
                    return item
            return None
        else:
            return cls(value=value)
