import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abc123@!",
        database="UniversityDB"
    )

def get_student_records(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT md.Module, md.Year, md.Semester, md.GradePoints, mm.Credits
    FROM ModuleDetails md
    JOIN ModuleMaster mm ON md.Module = mm.Module
    WHERE md.StudentID = %s
    ''', (student_id,))
    records = cursor.fetchall()
    conn.close()
    return records

def get_all_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT StudentID, StudentName, StudentEmail, School, Programme FROM StudentMaster')
    students = cursor.fetchall()
    conn.close()
    return students