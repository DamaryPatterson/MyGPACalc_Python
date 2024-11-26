from database import get_student_records, get_all_students
from gpa_calculator import calculate_cumulative_gpa, calculate_semester_gpa
from email_alerts import send_gpa_alert

def main():
    user_type = input("Are you a student or admin? ").strip().lower()
    if user_type == 'admin':
        students = get_all_students()
        for student in students:
            student_id = student[0]
            gpa, total_grade_points, total_credits = calculate_cumulative_gpa(student_id)
            if gpa <= 2.0:
                send_gpa_alert(student, gpa)
                print(f"Alert sent for student {student_id} with GPA {gpa}")
            print(f"Student ID: {student_id}, Total Grade Points: {total_grade_points}, Total Credits: {total_credits}, GPA: {gpa}")
            
            # Calculate and display GPA for each semester
            for year in range(2024, 2025):  # Adjust the range as needed
                for semester in range(1, 3):
                    semester_gpa, semester_total_grade_points, semester_total_credits = calculate_semester_gpa(student_id, year, semester)
                    print(f"Year: {year}, Semester: {semester}, GPA: {semester_gpa}, Total Grade Points: {semester_total_grade_points}, Total Credits: {semester_total_credits}")
    elif user_type == 'student':
        student_id = input("Enter your student ID: ")
        gpa, total_grade_points, total_credits = calculate_cumulative_gpa(student_id)
        print(f"Your cumulative GPA is {gpa}")
        print(f"Total Grade Points: {total_grade_points}, Total Credits: {total_credits}")
        
        # Calculate and display GPA for each semester
        for year in range(2024, 2025):  # Adjust the range as needed
            for semester in range(1, 3):
                semester_gpa, semester_total_grade_points, semester_total_credits = calculate_semester_gpa(student_id, year, semester)
                print(f"Year: {year}, Semester: {semester}, GPA: {semester_gpa}, Total Grade Points: {semester_total_grade_points}, Total Credits: {semester_total_credits}")
    else:
        print("Invalid user type")

if __name__ == "__main__":
    main()