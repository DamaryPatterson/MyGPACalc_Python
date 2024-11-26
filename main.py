from admin import admin_menu
from student import student_menu

def main():
    user_type = input("Are you a student or admin? ").strip().lower()
    if user_type == 'admin':
        admin_menu()
    elif user_type == 'student':
        student_id = input("Enter your student ID: ")
        student_menu(student_id)
    else:
        print("Invalid user type")

if __name__ == "__main__":
    main()