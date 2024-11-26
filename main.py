import sqlite3
from pyswip import Prolog

def fetch_student_data(student_id, year):
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    
    query = """
    SELECT md.Module, md.Credits, md.GradePoints
    FROM ModuleDetails md
    JOIN StudentMaster sm ON md.StudentID = sm.StudentID
    WHERE sm.StudentID = ? AND md.Year = ?
    """
    cursor.execute(query, (student_id, year))
    data = cursor.fetchall()
    conn.close()
    return data

def calculate_gpa(data):
    prolog = Prolog()
    prolog.consult("gpa_calculator.pl")
    
    total_credits = sum([row[1] for row in data])
    total_grade_points = sum([row[1] * row[2] for row in data])
    
    prolog.assertz(f"total_credits({total_credits})")
    prolog.assertz(f"total_grade_points({total_grade_points})")
    
    result = list(prolog.query("calculate_gpa(GPA)"))
    return result[0]['GPA']

def main():
    student_id = input("Enter Student ID: ")
    year = input("Enter Year: ")
    
    data = fetch_student_data(student_id, year)
    if not data:
        print("No data found for the given student and year.")
        return
    
    gpa = calculate_gpa(data)
    print(f"GPA for Student ID {student_id} in Year {year}: {gpa}")

if __name__ == "__main__":
    main()