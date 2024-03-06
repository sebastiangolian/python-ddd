from dataclasses import dataclass
from datetime import datetime

from domain.value_object.student_status import StudentStatus
from shared.ddd.entity import Entity


@dataclass
class Student(Entity):
    username: str = ""
    email: str = ""
    status: StudentStatus = StudentStatus.NEW
    created_at: int = datetime.now().timestamp()

    def register(self) -> None:
        self.status = StudentStatus.REGISTERED

    def delete(self) -> None:
        self.status = StudentStatus.DELETED

    @staticmethod
    def create(username: str, email: str) -> "Student":
        student = Student(username=username, email=email)
        return student
