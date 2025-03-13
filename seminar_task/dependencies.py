from seminar_task.sql_repository import SQLRepository


async def get_students_repo():
    return SQLRepository('students')


async def get_teachers_repo():
    return SQLRepository('teachers')
