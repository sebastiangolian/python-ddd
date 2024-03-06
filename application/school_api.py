from application.commands.school_class_add_student import SchoolClassAddStudentCommand, SchoolClassAddStudentHandler
from application.commands.school_class_create import SchoolClassCreateCommand, SchoolClassCreateHandler
from application.commands.school_class_remove import SchoolClassRemoveCommand, SchoolClassRemoveHandler
from application.commands.school_class_remove_student import (
    SchoolClassRemoveStudentCommand,
    SchoolClassRemoveStudentHandler,
)
from application.commands.school_class_remove_students import (
    SchoolClassRemoveStudentsCommand,
    SchoolClassRemoveStudentsHandler,
)
from application.commands.school_class_update import SchoolClassUpdateCommand, SchoolClassUpdateHandler
from application.commands.student_create import StudentCreateCommand, StudentCreateHandler
from application.commands.student_remove import StudentRemoveCommand, StudentRemoveHandler
from application.commands.student_update import StudentUpdateCommand, StudentUpdateHandler
from application.queries.school_class_with_students import SchoolClassWithStudentsHandler, SchoolClassWithStudentsQuery
from infrastructure.repositories.school_class_repository import SchoolClassRepository
from infrastructure.repositories.student_repository import StudentRepository
from settings import DB


class SchoolAPI:
    def __init__(self) -> None:
        self.__school_class_repository = SchoolClassRepository(DB)
        self.__student_repository = StudentRepository(DB)

    ### school_class use cases ###

    async def create_school_class(self, command: SchoolClassCreateCommand):
        handler = SchoolClassCreateHandler(command, self.__school_class_repository)
        await handler.handle()
        return handler

    def get_school_classes(self):
        return self.__school_class_repository.get()

    def get_school_class(self, school_class_id: str):
        return self.__school_class_repository.get_by_id(school_class_id)

    async def update_school_class(self, command: SchoolClassUpdateCommand):
        return await SchoolClassUpdateHandler(command, self.__school_class_repository).handle()

    async def remove_school_class(self, command: SchoolClassRemoveCommand):
        return await SchoolClassRemoveHandler(command, self.__school_class_repository).handle()

    async def remove_students(self, command: SchoolClassRemoveStudentsCommand):
        return await SchoolClassRemoveStudentsHandler(command, self.__school_class_repository).handle()

    ### student use cases ###

    async def create_student(self, command: StudentCreateCommand):
        handler = StudentCreateHandler(command, self.__student_repository)
        await handler.handle()
        return handler

    def get_students(self):
        return self.__student_repository.get()

    def get_student(self, student_id: str):
        return self.__student_repository.get_by_id(student_id)

    async def update_student(self, command: StudentUpdateCommand):
        return await StudentUpdateHandler(command, self.__student_repository).handle()

    async def remove_student(self, command: StudentRemoveCommand):
        return await StudentRemoveHandler(command, self.__student_repository).handle()

    ### student in class use cases ###

    async def add_student_to_school_class(self, command: SchoolClassAddStudentCommand):
        return await SchoolClassAddStudentHandler(
            command, self.__school_class_repository, self.__student_repository
        ).handle()

    async def remove_student_from_school_class(self, command: SchoolClassRemoveStudentCommand):
        return await SchoolClassRemoveStudentHandler(
            command, self.__school_class_repository, self.__student_repository
        ).handle()

    def get_school_class_with_students(self, query: SchoolClassWithStudentsQuery):
        return SchoolClassWithStudentsHandler(query, self.__school_class_repository, self.__student_repository).get()
