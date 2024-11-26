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



# import customtkinter as ctk
# from admin_ui import AdminUI
# from student_ui import StudentUI

# def main():
#     app = ctk.CTk()
#     app.geometry("800x600")
#     app.title("University GPA Management System")

#     def open_admin_ui():
#         admin_ui = AdminUI(app)
#         admin_ui.pack(fill="both", expand=True)

#     def open_student_ui():
#         student_ui = StudentUI(app)
#         student_ui.pack(fill="both", expand=True)

#     frame = ctk.CTkFrame(app)
#     frame.pack(pady=20, padx=60, fill="both", expand=True)

#     label = ctk.CTkLabel(frame, text="Welcome to the University GPA Management System", font=("Arial", 24))
#     label.pack(pady=20)

#     admin_button = ctk.CTkButton(frame, text="Admin", command=open_admin_ui)
#     admin_button.pack(pady=10)

#     student_button = ctk.CTkButton(frame, text="Student", command=open_student_ui)
#     student_button.pack(pady=10)

#     app.mainloop()

# if __name__ == "__main__":
#     main()