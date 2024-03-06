import json

from infrastructure.db.db_interface import DbInterface


def test_add(memory_db: DbInterface):
    _add_items(memory_db)
    memory_db.set_resource("students")
    assert memory_db.count() == 2
    memory_db.set_resource("products")
    assert memory_db.count() == 2


def test_count(memory_db: DbInterface):
    _add_items(memory_db)

    memory_db.set_resource("products")
    assert memory_db.count() == 2
    memory_db.set_resource("orders")
    assert memory_db.count() == 0


def test_get_by_id(memory_db: DbInterface):
    _add_items(memory_db)

    memory_db.set_resource("students")
    student = memory_db.get_by_id(1)
    assert student == {"id": 1, "name": "John Doe"}

    memory_db.set_resource("products")
    product = memory_db.get_by_id(2)
    assert product == {"id": 2, "name": "Product B"}


def test_get_by_attribute(memory_db: DbInterface):
    _add_items(memory_db)

    memory_db.set_resource("students")
    student = memory_db.get_by_attribute("name", "Jane Smith")
    assert student == [{"id": 2, "name": "Jane Smith"}]

    memory_db.set_resource("products")
    product = memory_db.get_by_attribute("name", "Product A")
    assert product == [{"id": 1, "name": "Product A"}]


def test_get_all_items(memory_db: DbInterface):
    _add_items(memory_db)

    expected_items = {
        "students": [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}],
        "products": [{"id": 1, "name": "Product A"}, {"id": 2, "name": "Product B"}],
    }
    assert memory_db.get_all_items() == json.dumps(expected_items, indent=2)


def test_remove(memory_db: DbInterface):
    _add_items(memory_db)

    memory_db.set_resource("students")
    memory_db.remove(2)

    assert memory_db.count() == 1


def test_clear(memory_db: DbInterface):
    _add_items(memory_db)

    memory_db.set_resource("students")
    memory_db.clear()

    assert memory_db.count() == 0


def _add_items(memory_db: DbInterface):
    memory_db.set_resource("students")
    memory_db.add({"id": 1, "name": "John Doe"})
    memory_db.add({"id": 2, "name": "Jane Smith"})

    memory_db.set_resource("products")
    memory_db.add({"id": 1, "name": "Product A"})
    memory_db.add({"id": 2, "name": "Product B"})
