import pytest

from application.commands.student_create import StudentCreateCommand, StudentCreateHandler
from domain.entity.student import Student
from domain.student_repository_interface import StudentRepositoryInterface
from shared.exceptions import ValidationException

USERNAME = "teststudent"


@pytest.mark.asyncio
async def test_create_valid_command(student_repository_mock: StudentRepositoryInterface):
    command = StudentCreateCommand(username=USERNAME, email="teststudent@example.com")
    service = StudentCreateHandler(command, student_repository_mock)

    try:
        await service.handle()
    except ValidationException:
        pytest.fail("ValidationException raised unexpectedly")

    assert student_repository_mock.find_by_attribute("username", USERNAME)


@pytest.mark.asyncio
async def test_create_validation_exception(student_repository_mock: StudentRepositoryInterface):
    command = StudentCreateCommand(username=USERNAME, email="teststudentexample.com")
    service = StudentCreateHandler(command, student_repository_mock)

    with pytest.raises(ValidationException) as exc_info:
        await service.handle()

    assert exc_info.value.errors == ["Invalid email address"]
    assert not student_repository_mock.find_by_attribute("username", USERNAME)


def test_validate_with_valid_data(student_repository_mock: StudentRepositoryInterface):
    command = StudentCreateCommand(email="test@example.com", username="teststudent")
    service = StudentCreateHandler(command, student_repository_mock)
    try:
        service.validate()
    except ValidationException:
        pytest.fail("ValidationException raised unexpectedly")


def test_validate_with_invalid_email(student_repository_mock: StudentRepositoryInterface):
    command = StudentCreateCommand(email="invalid_email", username="teststudent")
    service = StudentCreateHandler(command, student_repository_mock)

    with pytest.raises(ValidationException) as exc_info:
        service.validate()

    assert exc_info.value.errors == ["Invalid email address"]


def test_validate_with_existing_email(student_repository_mock: StudentRepositoryInterface):
    student_repository_mock.save(Student(id=1, email="test@example.com"))

    command = StudentCreateCommand(email="test@example.com", username="teststudent")
    service = StudentCreateHandler(command, student_repository_mock)

    with pytest.raises(ValidationException) as exc_info:
        service.validate()

    assert exc_info.value.errors == ["This email already exist"]


def test_validate_with_invalid_username(student_repository_mock: StudentRepositoryInterface):
    command = StudentCreateCommand(email="test@example.com", username="us")
    service = StudentCreateHandler(command, student_repository_mock)

    with pytest.raises(ValidationException) as exc_info:
        service.validate()

    assert exc_info.value.errors == ["Invalid username"]
