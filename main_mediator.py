from application.commands.school_class_add_student import SchoolClassAddStudentCommand, SchoolClassAddStudentHandler
from application.commands.school_class_create import SchoolClassCreateCommand, SchoolClassCreateHandler
from application.commands.student_create import StudentCreateCommand, StudentCreateHandler
from domain.school_class_repository_interface import SchoolClassRepositoryInterface
from domain.student_repository_interface import StudentRepositoryInterface
from infrastructure.db.memory_db import MemoryDb
from infrastructure.repositories.school_class_repository import SchoolClassRepository
from infrastructure.repositories.student_repository import StudentRepository
from shared.mediator import Mediator


async def main():
    mediator = Mediator()
    db = MemoryDb()
    mediator.register_service(SchoolClassRepositoryInterface, SchoolClassRepository(db))
    mediator.register_service(StudentRepositoryInterface, StudentRepository(db))
    mediator.bind(SchoolClassAddStudentCommand, SchoolClassAddStudentHandler)
    mediator.bind(StudentCreateCommand, StudentCreateHandler)
    mediator.bind(SchoolClassCreateCommand, SchoolClassCreateHandler)

    handler_student_create = await mediator.dispatch(StudentCreateCommand(username="dasdasd", email="test@email.com"))
    handler_school_class_create = await mediator.dispatch(SchoolClassCreateCommand(name="School 1", students_ids=[]))
    student = handler_student_create.student
    school_class = handler_school_class_create.school_class
    await mediator.dispatch(SchoolClassAddStudentCommand(school_class_id=school_class.id, student_id=student.id))

    print(MemoryDb().get_all_items())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
