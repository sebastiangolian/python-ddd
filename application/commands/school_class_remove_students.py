from dataclasses import dataclass
from typing import List

from domain.school_class_repository_interface import SchoolClassRepositoryInterface
from domain.student_repository_interface import StudentRepositoryInterface
from shared import validators
from shared.ddd.bussiness_rule import BusinessRule
from shared.ddd.command_handler import CommandHandler


@dataclass
class SchoolClassRemoveStudentsCommand:
    school_class_id: str


class SchoolClassRemoveStudentsHandler(CommandHandler, BusinessRule):
    def __init__(
        self, command: SchoolClassRemoveStudentsCommand, school_class_repository: SchoolClassRepositoryInterface
    ) -> None:
        self.__command = command
        self.__school_class_repository = school_class_repository

    @property
    def validators(self) -> List[tuple]:
        return [
            (
                not validators.is_exist_in_db(self.__command.school_class_id, self.__school_class_repository),
                "School class is not exist",
            ),
            (
                not validators.is_string(self.__command.school_class_id),
                "Param school_class_id is not a string",
            ),
        ]

    async def handle(self) -> None:
        self.validate()
        school_class = self.__school_class_repository.get_by_id(self.__command.school_class_id)
        school_class.remove_students()
        self.__school_class_repository.save(school_class)
