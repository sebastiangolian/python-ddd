from domain.entity.student import Student


def test_student_create():
    student = Student(username="john_rambo", email="johnrambo@gmail.com")
    assert student.created_at is not None
    assert student.status.is_new


def test_student_register():
    student = Student(username="john_rambo", email="johnrambo@gmail.com")
    student.register()
    assert student.status.is_registered


def test_student_delete():
    student = Student(username="john_rambo", email="johnrambo@gmail.com")
    student.delete()
    assert student.status.is_deleted
