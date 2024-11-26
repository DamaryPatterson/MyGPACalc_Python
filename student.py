from gpa_calculator import calculate_cumulative_gpa, calculate_semester_gpa, get_default_gpa

def student_menu(student_id):
    gpa, total_grade_points, total_credits = calculate_cumulative_gpa(student_id)
    default_gpa = get_default_gpa()
    print(f"University of Technology\nAcademic Probation Alert GPA Report\n")
    print(f"Student ID: {student_id}")
    print(f"Total Grade Points: {total_grade_points:.3f}, Total Credits: {total_credits:.3f}, Cumulative GPA: {gpa:.3f}")
    if gpa <= default_gpa:
        print("Status: On Academic Probation")
    else:
        print("Status: In Good Standing")
    
    # Calculate and display GPA for each semester
    for year in range(2024, 2025):  # Adjust the range as needed
        for semester in range(1, 3):
            semester_gpa, semester_total_grade_points, semester_total_credits = calculate_semester_gpa(student_id, year, semester)
            print(f"Year: {year}, Semester: {semester}, GPA: {semester_gpa:.3f}, Total Grade Points: {semester_total_grade_points:.3f}, Total Credits: {semester_total_credits:.3f}")