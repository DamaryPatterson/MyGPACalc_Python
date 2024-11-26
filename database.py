import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abc123@!",
        database="UniversityDB"
    )

# CRUD operations for StudentMaster
def create_student(student_id, student_name, student_email, school, programme):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO StudentMaster (StudentID, StudentName, StudentEmail, School, Programme)
    VALUES (%s, %s, %s, %s, %s)
    ''', (student_id, student_name, student_email, school, programme))
    conn.commit()
    conn.close()

def read_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM StudentMaster')
    students = cursor.fetchall()
    conn.close()
    return students

def update_student(student_id, student_name, student_email, school, programme):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE StudentMaster
    SET StudentName = %s, StudentEmail = %s, School = %s, Programme = %s
    WHERE StudentID = %s
    ''', (student_name, student_email, school, programme, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM StudentMaster WHERE StudentID = %s', (student_id,))
    conn.commit()
    conn.close()

# CRUD operations for ModuleMaster
def create_module(module, credits):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO ModuleMaster (Module, Credits)
    VALUES (%s, %s)
    ''', (module, credits))
    conn.commit()
    conn.close()

def read_modules():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ModuleMaster')
    modules = cursor.fetchall()
    conn.close()
    return modules

def update_module(module, credits):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE ModuleMaster
    SET Credits = %s
    WHERE Module = %s
    ''', (credits, module))
    conn.commit()
    conn.close()

def delete_module(module):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM ModuleMaster WHERE Module = %s', (module,))
    conn.commit()
    conn.close()

# CRUD operations for ModuleDetails
def create_module_detail(module, year, semester, student_id, grade_points):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO ModuleDetails (Module, Year, Semester, StudentID, GradePoints)
    VALUES (%s, %s, %s, %s, %s)
    ''', (module, year, semester, student_id, grade_points))
    conn.commit()
    conn.close()

def read_module_details():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ModuleDetails')
    module_details = cursor.fetchall()
    conn.close()
    return module_details

def update_module_detail(module, year, semester, student_id, grade_points):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE ModuleDetails
    SET GradePoints = %s
    WHERE Module = %s AND Year = %s AND Semester = %s AND StudentID = %s
    ''', (grade_points, module, year, semester, student_id))
    conn.commit()
    conn.close()

def delete_module_detail(module, year, semester, student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM ModuleDetails
    WHERE Module = %s AND Year = %s AND Semester = %s AND StudentID = %s
    ''', (module, year, semester, student_id))
    conn.commit()
    conn.close()

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

# Functions for StudentGPA
def save_student_gpa(student_id, year, gpa):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO StudentGPA (StudentID, Year, GPA)
    VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE GPA = %s
    ''', (student_id, year, gpa, gpa))
    conn.commit()
    conn.close()

def read_student_gpa(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM StudentGPA WHERE StudentID = %s', (student_id,))
    gpa_records = cursor.fetchall()
    conn.close()
    return gpa_records