from dataclasses import dataclass
from typing import List

from domain.school_class_repository_interface import SchoolClassRepositoryInterface
from domain.student_repository_interface import StudentRepositoryInterface
from shared import validators
from shared.ddd.bussiness_rule import BusinessRule
from shared.ddd.query_handler import PaginationQuery, QueryHandler


@dataclass
class SchoolClassWithStudentsQuery(PaginationQuery):
    pass


class SchoolClassWithStudentsHandler(QueryHandler, BusinessRule):
    def __init__(
        self,
        query: SchoolClassWithStudentsQuery,
        school_class_repository: SchoolClassRepositoryInterface,
        student_repository: StudentRepositoryInterface,
    ) -> None:
        self.__query = query
        self.__school_class_repository = school_class_repository
        self.__student_repository = student_repository

    @property
    def validators(self) -> List[tuple]:
        return [
            (
                not validators.is_integer(self.__query.limit),
                "Param limit is not integer",
            ),
            (
                not validators.is_integer(self.__query.page),
                "Param page is not integer",
            ),
        ]

    def get(self) -> List[dict]:
        self.validate()

        school_class_models = self.__school_class_repository.get(self.__query.limit, self.__query.page)
        student_models = self.__student_repository.get_by_ids(
            set(student_id for school_class in school_class_models for student_id in school_class.students_ids)
        )

        return_list = []
        students_dict = {student.id: student.to_dict() for student in student_models}

        for school_class in school_class_models:
            class_dict = school_class.to_dict()
            class_dict["students"] = [students_dict[student_id] for student_id in school_class.students_ids]

            return_list.append(class_dict)

        return return_list
