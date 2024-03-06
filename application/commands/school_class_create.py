from dataclasses import dataclass, field
from typing import List, Union

from domain.entity.school_class import SchoolClass
from domain.school_class_repository_interface import SchoolClassRepositoryInterface
from shared import validators
from shared.ddd.bussiness_rule import BusinessRule
from shared.ddd.command_handler import CommandHandler


@dataclass
class SchoolClassCreateCommand:
    name: str = ""
    students_ids: List[str] = field(default_factory=list)


class SchoolClassCreateHandler(CommandHandler, BusinessRule):
    def __init__(
        self,
        command: SchoolClassCreateCommand,
        school_class_repository: SchoolClassRepositoryInterface,
    ) -> None:
        self.__school_class_repository = school_class_repository
        self.__command = command
        self.__school_class = None

    @property
    def school_class(self) -> Union[None, SchoolClass]:
        return self.__school_class

    @property
    def validators(self) -> List[tuple]:
        return [
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
        self.__school_class = SchoolClass.create(name=self.__command.name, students_ids=self.__command.students_ids)
        self.__school_class_repository.save(self.__school_class)
