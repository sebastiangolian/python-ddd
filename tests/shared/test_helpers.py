import pytest

from shared.helpers import find_object


@pytest.fixture
def objects_list():
    return [
        {"id": "zzz", "name": "zzz", "status": None},
        {"id": "xxx", "name": "johnrambo", "status": "warrior"},
        {"id": "john", "name": "john", "status": None},
        {"id": "johnrambo", "name": "rambo", "status": "warrior"},
    ]


def test_find_object(objects_list):
    expected_object = {"id": "xxx", "name": "johnrambo", "status": "warrior"}
    object_field = "name"
    expected_value = "johnrambo"
    result = find_object(objects_list, object_field, expected_value)

    assert result == expected_object
