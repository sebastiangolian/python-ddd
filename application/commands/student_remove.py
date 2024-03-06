from dataclasses import dataclass
from typing import List

from domain.student_repository_interface import StudentRepositoryInterface
from shared import validators
from shared.ddd.command_handler import CommandHandler


@dataclass
class StudentRemoveCommand:
    student_id: str


class StudentRemoveHandler(CommandHandler):
    def __init__(self, command: StudentRemoveCommand, student_repository: StudentRepositoryInterface) -> None:
        self.__command = command
        self.__student_repository = student_repository

    @property
    def validators(self) -> List[tuple]:
        return [
            (
                not validators.is_string(self.__command.student_id),
                "Invalid student_id param",
            ),
            (
                not validators.is_exist_in_db(self.__command.student_id, self.__student_repository),
                "This student not exist",
            ),
        ]

    async def handle(self) -> None:
        self.validate()
        student = self.__student_repository.get_by_id(self.__command.student_id)
        student.delete()
        self.__student_repository.save(student)
