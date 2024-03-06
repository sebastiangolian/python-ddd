import json
from typing import Any, List, Optional

from infrastructure.db.db_interface import DbInterface
from shared.decorators import singleton
from shared.helpers import find_object, find_objects, remove_object


@singleton
class MemoryDb(DbInterface):
    def __init__(self) -> None:
        self.__resource = "default"
        self.__items = {}
        self.__counter = 0

    def set_resource(self, resource: str) -> "MemoryDb":
        self.__resource = resource
        return self

    def count(self) -> int:
        return len(self.__items.get(self.__resource, []))

    def get(self, limit: Optional[int] = None, page: Optional[int] = None) -> List[object]:
        items = self.__items.get(self.__resource, [])

        if limit is not None and page is not None:
            start_index = (page - 1) * limit
            end_index = start_index + limit
            items = items[start_index:end_index]

        return items

    def get_all_items(self) -> str:
        return json.dumps(self.__items, indent=2)

    def get_by_id(self, id: int) -> object:
        return find_object(self.__items.get(self.__resource, []), "id", id)

    def get_by_ids(self, ids: List[int]) -> List[object]:
        return [item for item in self.__items.get(self.__resource, []) if item.get("id") in ids]

    def get_by_attribute(self, attribute: str, value: Any) -> List[object]:
        return find_objects(self.__items.get(self.__resource, []), attribute, value)

    def add(self, item: object) -> None:
        if item.get("id") is None:
            item["id"] = self.__counter
            self.__counter += 1

        if self.__items.get(self.__resource):
            self.__items[self.__resource].append(item)
        else:
            self.__items[self.__resource] = [item]

    def update(self, id: int, item: object) -> None:
        items = self.__items.get(self.__resource, [])
        index = self._find_index(items, "id", id)
        if index is not None:
            items[index] = item
        else:
            raise ValueError(f"Item with id {id} not found.")

    def remove(self, id: int) -> None:
        self.__items[self.__resource] = remove_object(self.__items.get(self.__resource, []), "id", id)

    def clear(self) -> None:
        self.__items = {}

    def _find_index(self, items: List[object], attribute: str, value: Any) -> Optional[int]:
        for i, item in enumerate(items):
            if item.get(attribute) == value:
                return i
        return None
