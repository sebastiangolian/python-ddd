from dataclasses import dataclass
from typing import List

from domain.student_repository_interface import StudentRepositoryInterface
from shared import validators
from shared.ddd.command_handler import CommandHandler


@dataclass
class SchoolClassRemoveCommand:
    school_class_id: str


class SchoolClassRemoveHandler(CommandHandler):
    def __init__(self, command: SchoolClassRemoveCommand, school_class_repository: StudentRepositoryInterface) -> None:
        self.__command = command
        self.__repository = school_class_repository

    @property
    def validators(self) -> List[tuple]:
        return [
            (
                not validators.is_string(self.__command.school_class_id),
                "Invalid school_class_id param",
            ),
            (
                not validators.is_exist_in_db(self.__command.school_class_id, self.__repository),
                "This school_class not exist",
            ),
        ]

    async def handle(self) -> None:
        self.validate()
        self.__repository.remove(self.__command.school_class_id)
