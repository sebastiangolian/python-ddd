import re
from typing import Any

from shared.ddd.generic_repository import GenericRepository


def is_exist_in_db_by_property(property: str, value: Any, repository: GenericRepository) -> bool:
    return bool(repository.find_by_attribute(property, value))


def is_exist_in_db(id: Any, repository: GenericRepository) -> bool:
    return bool(repository.get_by_id(id))


def is_string(param: Any) -> bool:
    return isinstance(param, str)


def is_string_grather_than(str: str, length: int) -> bool:
    return len(str) > length


def is_valid_email(email: str) -> bool:
    email_pattern = re.compile(r"^[\w.-]+@[a-zA-Z_-]+?\.[a-zA-Z]{2,3}$")
    return bool(re.match(email_pattern, email))


def is_integer(param: Any) -> bool:
    return isinstance(param, int)


def is_list_of_int_or_empty(param: Any) -> bool:
    return isinstance(param, list) and (not param or all(isinstance(item, int) for item in param))


def is_list_of_str_or_empty(param: Any) -> bool:
    return isinstance(param, list) and (not param or all(isinstance(item, str) for item in param))
