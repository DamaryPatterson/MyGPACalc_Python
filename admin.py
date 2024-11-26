from database import (
    create_student, read_students, save_student_gpa, update_student, delete_student,
    create_module, read_modules, update_module, delete_module,
    create_module_detail, read_module_details, update_module_detail, delete_module_detail,
)
from gpa_calculator import calculate_cumulative_gpa

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Create Student")
        print("2. Read Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Create Module")
        print("6. Read Modules")
        print("7. Update Module")
        print("8. Delete Module")
        print("9. Create Module Detail")
        print("10. Read Module Details")
        print("11. Update Module Detail")
        print("12. Delete Module Detail")
        print("13. Record Student GPA")
        print("14. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            student_email = input("Enter Student Email: ")
            school = input("Enter School: ")
            programme = input("Enter Programme: ")
            create_student(student_id, student_name, student_email, school, programme)
        elif choice == '2':
            students = read_students()
            for student in students:
                print(student)
        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            student_name = input("Enter new Student Name: ")
            student_email = input("Enter new Student Email: ")
            school = input("Enter new School: ")
            programme = input("Enter new Programme: ")
            update_student(student_id, student_name, student_email, school, programme)
        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)
        elif choice == '5':
            module = input("Enter Module: ")
            credits = int(input("Enter Credits: "))
            create_module(module, credits)
        elif choice == '6':
            modules = read_modules()
            for module in modules:
                print(module)
        elif choice == '7':
            module = input("Enter Module to update: ")
            credits = int(input("Enter new Credits: "))
            update_module(module, credits)
        elif choice == '8':
            module = input("Enter Module to delete: ")
            delete_module(module)
        elif choice == '9':
            module = input("Enter Module: ")
            year = int(input("Enter Year: "))
            semester = int(input("Enter Semester: "))
            student_id = input("Enter Student ID: ")
            grade_points = float(input("Enter Grade Points: "))
            create_module_detail(module, year, semester, student_id, grade_points)
        elif choice == '10':
            module_details = read_module_details()
            for detail in module_details:
                print(detail)
        elif choice == '11':
            module = input("Enter Module to update: ")
            year = int(input("Enter Year: "))
            semester = int(input("Enter Semester: "))
            student_id = input("Enter Student ID: ")
            grade_points = float(input("Enter new Grade Points: "))
            update_module_detail(module, year, semester, student_id, grade_points)
        elif choice == '12':
            module = input("Enter Module to delete: ")
            year = int(input("Enter Year: "))
            semester = int(input("Enter Semester: "))
            student_id = input("Enter Student ID: ")
            delete_module_detail(module, year, semester, student_id)
        elif choice == '13':
            student_id = input("Enter Student ID: ")
            year = int(input("Enter Year: "))
            desired_gpa = input("Enter desired GPA (optional): ")
            if desired_gpa:
                desired_gpa = float(desired_gpa)
            else:
                desired_gpa = 2.0  # Default GPA
            gpa, total_grade_points, total_credits = calculate_cumulative_gpa(student_id)
            save_student_gpa(student_id, year, gpa)
            print(f"Student ID: {student_id}, Year: {year}, Desired GPA: {desired_gpa}")
            print(f"Total Grade Points: {total_grade_points:.3f}, Total Credits: {total_credits:.3f}, GPA: {gpa:.3f}")
        elif choice == '14':
            break
        else:
            print("Invalid choice. Please try again.")