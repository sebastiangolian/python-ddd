from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from shared.ddd.entity import Entity
from shared.exceptions import ValidationException


@dataclass
class SchoolClass(Entity):
    name: str = ""
    school_id: int = 0
    students_ids: List[str] = field(default_factory=list)
    created_at: int = field(default_factory=lambda: int(datetime.now().timestamp()))

    @staticmethod
    def create(name: str, students_ids: List[str]) -> "SchoolClass":
        return SchoolClass(name=name, students_ids=students_ids)

    def add_student(self, student_id: str) -> None:
        if student_id in self.students_ids:
            raise ValidationException(errors=["Student is already in the class."])
        self.students_ids.append(student_id)

    def remove_student(self, student_id: str) -> None:
        if student_id not in self.students_ids:
            raise ValidationException(errors=["Student is not in the class."])
        self.students_ids.remove(student_id)

    def remove_students(self) -> None:
        self.students_ids = []
