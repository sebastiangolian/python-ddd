import pytest

from domain.entity.student import Student
from infrastructure.repositories.student_repository import StudentRepository


class TestStudentRepository:
    @pytest.fixture
    def student_setup(self, memory_db):
        student = Student(username="john_rambo", email="johnrambo@gmail.com")
        repo = StudentRepository(memory_db)
        repo.save(student)

        self.memory_db = memory_db
        self.student = student
        self.repo = repo

    def test_count(self, student_setup):
        assert self.repo.count == 1

    def test_get(self, student_setup):
        found_student = self.repo.get_by_id(self.student.id)
        assert found_student.username == self.student.username
        assert found_student.email == self.student.email

    def test_find_by_username(self, student_setup):
        found_student = self.repo.find_by_attribute("username", self.student.username)
        assert found_student[0].username == self.student.username
        assert found_student[0].email == self.student.email

    def test_find_by_email(self, student_setup):
        found_student = self.repo.find_by_attribute("email", self.student.email)
        assert found_student[0].username == self.student.username
        assert found_student[0].email == self.student.email

    def test_save_student(self, student_setup):
        assert self.repo.count == 1
