from dataclasses import dataclass
from typing import List, Union

from domain.entity.student import Student
from domain.student_repository_interface import StudentRepositoryInterface
from domain.value_object.student_status import StudentStatus
from shared import validators
from shared.ddd.bussiness_rule import BusinessRule
from shared.ddd.command_handler import CommandHandler


@dataclass
class StudentUpdateCommand:
    student_id: int
    username: str = ""
    email: str = ""


class StudentUpdateHandler(CommandHandler, BusinessRule):
    def __init__(self, command: StudentUpdateCommand, student_repository: StudentRepositoryInterface) -> None:
        self.__command = command
        self.__student_repository = student_repository
        self.__student = None

    @property
    def student(self) -> Union[None, Student]:
        return self.__student

    async def handle(self) -> None:
        self.validate()
        self.__student = self.__student_repository.get_by_id(self.__command.student_id)
        self.__student.email = self.__command.email
        self.__student.username = self.__command.username
        self.__student_repository.save(self.__student)

    @property
    def validators(self) -> List[tuple]:
        return [
            (
                not validators.is_exist_in_db(self.__command.student_id, self.__student_repository),
                "This student not exist",
            ),
            (
                not validators.is_valid_email(self.__command.email),
                "Invalid email address",
            ),
            (
                self._is_username_exist(),
                "This username already exist",
            ),
            (
                self._is_email_exist(),
                "This email already exist",
            ),
            (
                not validators.is_string_grather_than(self.__command.username, 2),
                "Invalid username",
            ),
        ]

    def _is_username_exist(self) -> bool:
        students = self.__student_repository.find_by_attribute("username", self.__command.username)
        students = [u for u in students if u.status != StudentStatus.DELETED]
        return len(students) > 1

    def _is_email_exist(self) -> bool:
        students = self.__student_repository.find_by_attribute("email", self.__command.email)
        students = [u for u in students if u.status != StudentStatus.DELETED]
        return len(students) > 1
