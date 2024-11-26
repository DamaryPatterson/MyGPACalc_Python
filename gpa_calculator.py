from pyswip import Prolog
from database import get_student_records

prolog = Prolog()

def calculate_gpa(records):
    prolog.consult("gpa_calculator.pl")
    
    # Prepare the list of grade points and credits for Prolog
    grades_and_credits = [[record[3], record[4]] for record in records]
    
    # Convert the list to a Prolog-readable format
    prolog_list = str(grades_and_credits).replace('[', '[').replace(']', ']')
    
    # Calculate total grade points and total credits
    result = list(prolog.query(f"calculate_totals({prolog_list}, TotalGradePoints, TotalCredits)"))
    if not result:
        return 0, 0, 0
    
    total_grade_points = result[0]['TotalGradePoints']
    total_credits = result[0]['TotalCredits']
    
    # Calculate GPA
    gpa_result = list(prolog.query(f"calculate_gpa({total_grade_points}, {total_credits}, GPA)"))
    if not gpa_result:
        return 0, total_grade_points, total_credits
    
    gpa = gpa_result[0]['GPA']
    return gpa, total_grade_points, total_credits

def calculate_semester_gpa(student_id, year, semester):
    records = get_student_records(student_id)
    semester_records = [record for record in records if record[1] == year and record[2] == semester]
    return calculate_gpa(semester_records)

def calculate_cumulative_gpa(student_id):
    records = get_student_records(student_id)
    return calculate_gpa(records)
