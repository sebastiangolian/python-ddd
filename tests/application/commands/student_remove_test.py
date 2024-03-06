import pytest

from application.commands.student_remove import StudentRemoveCommand, StudentRemoveHandler
from domain.entity.student import Student
from domain.student_repository_interface import StudentRepositoryInterface
from shared.exceptions import ValidationException


@pytest.mark.asyncio
async def test_student_remove_valid_command(student_repository_mock: StudentRepositoryInterface):
    student_repository_mock.save(Student(id="1"))

    command = StudentRemoveCommand(student_id="1")
    service = StudentRemoveHandler(command, student_repository_mock)

    try:
        await service.handle()
    except ValidationException:
        pytest.fail("ValidationException raised unexpectedly")

    assert not student_repository_mock.find_by_attribute("student_id", 1)


@pytest.mark.asyncio
async def test_student_remove_invalid_command(student_repository_mock: StudentRepositoryInterface):
    student_repository_mock.save(Student(id="2"))

    command = StudentRemoveCommand(student_id="1")
    service = StudentRemoveHandler(command, student_repository_mock)

    with pytest.raises(ValidationException) as exc_info:
        await service.handle()

    assert exc_info.value.errors == ["This student not exist"]


def test_validate_with_valid_data(student_repository_mock: StudentRepositoryInterface):
    student_repository_mock.save(Student(id="1"))
    command = StudentRemoveCommand(student_id="1")
    service = StudentRemoveHandler(command, student_repository_mock)

    try:
        service.validate()
    except ValidationException:
        pytest.fail("ValidationException raised unexpectedly")


def test_validate_with_invalid_student_id(student_repository_mock: StudentRepositoryInterface):
    command = StudentRemoveCommand(student_id=1)
    service = StudentRemoveHandler(command, student_repository_mock)

    with pytest.raises(ValidationException) as exc_info:
        service.validate()

    assert exc_info.value.errors == ["Invalid student_id param", "This student not exist"]


def test_validate_with_not_existing_student(student_repository_mock: StudentRepositoryInterface):
    command = StudentRemoveCommand(student_id="1")
    service = StudentRemoveHandler(command, student_repository_mock)

    with pytest.raises(ValidationException) as exc_info:
        service.validate()

    assert exc_info.value.errors == ["This student not exist"]
