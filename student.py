from gpa_calculator import calculate_cumulative_gpa, calculate_semester_gpa

def student_menu(student_id):
    gpa, total_grade_points, total_credits = calculate_cumulative_gpa(student_id)
    print(f"Your cumulative GPA is {gpa:.3f}")
    print(f"Total Grade Points: {total_grade_points:.3f}, Total Credits: {total_credits:.3f}")
    
    # Calculate and display GPA for each semester
    for year in range(2024, 2025):  # Adjust the range as needed
        for semester in range(1, 3):
            semester_gpa, semester_total_grade_points, semester_total_credits = calculate_semester_gpa(student_id, year, semester)
            print(f"Year: {year}, Semester: {semester}, GPA: {semester_gpa:.3f}, Total Grade Points: {semester_total_grade_points:.3f}, Total Credits: {semester_total_credits:.3f}")