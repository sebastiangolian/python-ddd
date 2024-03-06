import pytest

from domain.school_class_repository_interface import SchoolClassRepositoryInterface
from domain.student_repository_interface import StudentRepositoryInterface
from infrastructure.db.db_interface import DbInterface
from infrastructure.db.memory_db import MemoryDb
from infrastructure.repositories.school_class_repository import SchoolClassRepository
from infrastructure.repositories.student_repository import StudentRepository


@pytest.fixture
def memory_db() -> DbInterface:
    db = MemoryDb()
    yield db

    db.clear()


@pytest.fixture
def school_class_repository_mock(memory_db: DbInterface) -> SchoolClassRepositoryInterface:
    return SchoolClassRepository(memory_db)


@pytest.fixture
def student_repository_mock(memory_db: DbInterface) -> StudentRepositoryInterface:
    return StudentRepository(memory_db)
