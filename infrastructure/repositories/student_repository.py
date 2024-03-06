from typing import Any, List, Optional

from domain.entity.student import Student
from domain.student_repository_interface import StudentRepositoryInterface
from infrastructure.db.db_interface import DbInterface


class StudentRepository(StudentRepositoryInterface):
    TYPE = "students"

    def __init__(self, db: DbInterface) -> None:
        self.__db = db

    @property
    def count(self) -> int:
        return self.__db.set_resource(self.TYPE).count()

    def get(self, limit: Optional[int] = None, page: Optional[int] = None) -> List[Student]:
        school_classs_dicts = self.__db.set_resource(self.TYPE).get(limit, page)
        return [Student(**school_class_dict) for school_class_dict in school_classs_dicts]

    def get_by_id(self, id: int) -> Optional[Student]:
        student_dict = self.__db.set_resource(self.TYPE).get_by_id(id)
        if student_dict:
            return Student(**student_dict)
        else:
            return None

    def get_by_ids(self, ids: List[int]) -> List[Student]:
        school_classes_dicts = self.__db.set_resource(self.TYPE).get_by_ids(ids)
        return [Student(**school_class_dict) for school_class_dict in school_classes_dicts]

    def find_by_attribute(self, attribute: str, value: Any) -> List[Student]:
        students_dicts = self.__db.set_resource(self.TYPE).get_by_attribute(attribute, value)
        return [Student(**student_dict) for student_dict in students_dicts]

    def save(self, student: Student) -> None:
        student_finded = self.__db.set_resource(self.TYPE).get_by_id(student.id)
        if student_finded:
            self.__db.set_resource(self.TYPE).update(student.id, student.to_dict())
        else:
            self.__db.set_resource(self.TYPE).add(student.to_dict())

    def remove(self, id: int) -> None:
        self.__db.set_resource(self.TYPE).remove(id)
