from dataclasses import dataclass
from typing import List

from domain.school_class_repository_interface import SchoolClassRepositoryInterface
from domain.student_repository_interface import StudentRepositoryInterface
from shared import validators
from shared.ddd.bussiness_rule import BusinessRule
from shared.ddd.command_handler import CommandHandler


@dataclass
class SchoolClassAddStudentCommand:
    school_class_id: str
    student_id: str


class SchoolClassAddStudentHandler(CommandHandler, BusinessRule):
    def __init__(
        self,
        command: SchoolClassAddStudentCommand,
        school_class_repository: SchoolClassRepositoryInterface,
        student_repository: StudentRepositoryInterface,
    ) -> None:
        self.__command = command
        self.__school_class_repository = school_class_repository
        self.__student_repository = student_repository

    @property
    def validators(self) -> List[tuple]:
        return [
            (
                not validators.is_exist_in_db(self.__command.student_id, self.__student_repository),
                "Student is not exist",
            ),
            (
                not validators.is_string(self.__command.school_class_id),
                "Param school_class_id is not a string",
            ),
            (
                not validators.is_string(self.__command.student_id),
                "Param student_id is not a string",
            ),
        ]

    async def handle(self) -> None:
        self.validate()
        school_class = self.__school_class_repository.get_by_id(self.__command.school_class_id)
        school_class.add_student(self.__command.student_id)
        self.__school_class_repository.save(school_class)
