from application.commands.school_class_add_student import SchoolClassAddStudentCommand
from application.commands.school_class_create import SchoolClassCreateCommand
from application.commands.school_class_remove import SchoolClassRemoveCommand
from application.commands.school_class_remove_student import SchoolClassRemoveStudentCommand
from application.commands.school_class_remove_students import SchoolClassRemoveStudentsCommand
from application.commands.school_class_update import SchoolClassUpdateCommand
from application.commands.student_create import StudentCreateCommand
from application.commands.student_remove import StudentRemoveCommand
from application.commands.student_update import StudentUpdateCommand
from application.queries.school_class_with_students import SchoolClassWithStudentsQuery
from application.school_api import SchoolAPI


async def main():
    school_api = SchoolAPI()

    # # create
    await school_api.create_school_class(SchoolClassCreateCommand("school_class1", []))
    await school_api.create_school_class(SchoolClassCreateCommand("school_class2", []))
    await school_api.create_school_class(SchoolClassCreateCommand("school_class3", []))
    await school_api.create_school_class(SchoolClassCreateCommand("school_class4", []))
    await school_api.create_school_class(SchoolClassCreateCommand("school_class5", []))
    await school_api.create_student(StudentCreateCommand("student_1", "student1@gmail.com"))
    await school_api.create_student(StudentCreateCommand("student_2", "student2@gmail.com"))

    # # views
    school_classes = school_api.get_school_classes()
    school_class = school_api.get_school_class(school_classes[0].id)
    students = school_api.get_students()
    student = school_api.get_student(students[0].id)
    student2 = school_api.get_student(students[1].id)

    print(school_class)
    print(student, student2)

    # updates
    await school_api.update_school_class(SchoolClassUpdateCommand(school_class.id, "school_class1_update", []))
    await school_api.update_student(StudentUpdateCommand(student.id, "student_1_update", "student1@gmail.com"))
    await school_api.add_student_to_school_class(SchoolClassAddStudentCommand(school_class.id, student.id))
    await school_api.add_student_to_school_class(SchoolClassAddStudentCommand(school_class.id, student2.id))

    # views after update
    school_class = school_api.get_school_class(school_classes[0].id)
    student = school_api.get_student(students[0].id)
    print(school_class)
    print(student)

    # queries
    school_classes_with_students = school_api.get_school_class_with_students(SchoolClassWithStudentsQuery(10))
    print(school_classes_with_students)

    # removes
    await school_api.remove_student_from_school_class(SchoolClassRemoveStudentCommand(school_class.id, student.id))
    await school_api.remove_students(SchoolClassRemoveStudentsCommand(school_class.id))
    await school_api.remove_school_class(SchoolClassRemoveCommand(school_class.id))
    await school_api.remove_student(StudentRemoveCommand(student.id))

    school_classes = school_api.get_school_classes()
    print(len(school_classes))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
