from dataclasses import dataclass, field
from typing import List

from domain.school_class_repository_interface import SchoolClassRepositoryInterface
from shared import validators
from shared.ddd.bussiness_rule import BusinessRule
from shared.ddd.command_handler import CommandHandler


@dataclass
class SchoolClassUpdateCommand:
    id: int
    name: str = ""
    students_ids: List[str] = field(default_factory=list)


class SchoolClassUpdateHandler(CommandHandler, BusinessRule):
    def __init__(
        self,
        command: SchoolClassUpdateCommand,
        school_class_repository: SchoolClassRepositoryInterface,
    ) -> None:
        self.__school_class_repository = school_class_repository
        self.__command = command

    @property
    def validators(self) -> List[tuple]:
        return [
            (
                not validators.is_exist_in_db(self.__command.id, self.__school_class_repository),
                "This school_class not exist",
            ),
            (
                validators.is_exist_in_db_by_property("name", self.__command.name, self.__school_class_repository),
                "This name already exist",
            ),
            (
                not validators.is_list_of_str_or_empty(self.__command.students_ids),
                "Invalid students_ids",
            ),
        ]

    async def handle(self) -> None:
        self.validate()
        school_class = self.__school_class_repository.get_by_id(self.__command.id)
        school_class.name = self.__command.name
        school_class.students_ids = self.__command.students_ids
        self.__school_class_repository.save(school_class)
