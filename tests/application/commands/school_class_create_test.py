import pytest

from application.commands.school_class_create import SchoolClassCreateCommand, SchoolClassCreateHandler
from domain.school_class_repository_interface import SchoolClassRepositoryInterface
from shared.exceptions import ValidationException


@pytest.mark.asyncio
async def test_create_valid_command(school_class_repository_mock: SchoolClassRepositoryInterface):
    command = SchoolClassCreateCommand(name="school_1", students_ids=["1", "2", "3"])
    service = SchoolClassCreateHandler(command, school_class_repository_mock)
    await service.handle()

    school_class = school_class_repository_mock.find_by_attribute("name", "school_1")
    assert len(school_class) > 0


@pytest.mark.asyncio
async def test_create_invalid_command(school_class_repository_mock: SchoolClassRepositoryInterface):
    command = SchoolClassCreateCommand(name="school_1", students_ids=[1])
    service = SchoolClassCreateHandler(command, school_class_repository_mock)

    with pytest.raises(ValidationException):
        await service.handle()

    school_class = school_class_repository_mock.find_by_attribute("name", "school_1")
    assert len(school_class) == 0


def test_validate_with_valid_data(school_class_repository_mock: SchoolClassRepositoryInterface):
    command = SchoolClassCreateCommand(name="school_1", students_ids=[])
    service = SchoolClassCreateHandler(command, school_class_repository_mock)
    try:
        service.validate()
    except ValidationException:
        pytest.fail("ValidationException raised unexpectedly")


def test_validate_with_invalid_data(school_class_repository_mock: SchoolClassRepositoryInterface):
    command = SchoolClassCreateCommand(name="school_1", students_ids=[1])
    service = SchoolClassCreateHandler(command, school_class_repository_mock)

    with pytest.raises(ValidationException) as exc_info:
        service.validate()

    assert exc_info.value.errors == ["Invalid students_ids"]
