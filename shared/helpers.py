from typing import Any, List


def find_object(objects_list: List[object], object_field: str, expected_value: Any) -> object:
    return next((item for item in objects_list if item[object_field] == expected_value), {})


def find_objects(objects_list: List[object], object_field: str, expected_value: Any) -> List[object]:
    return [item for item in objects_list if item.get(object_field, []) == expected_value]


def remove_object(object_list: List[object], object_field: str, value: Any) -> List[object]:
    return list(filter(lambda obj: obj[object_field] != value, object_list))
