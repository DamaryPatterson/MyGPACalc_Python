import customtkinter as ctk
from gpa_calculator import calculate_cumulative_gpa, calculate_semester_gpa, get_default_gpa

class StudentUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.label = ctk.CTkLabel(self, text="Student Menu", font=("Arial", 24))
        self.label.pack(pady=20)

        self.student_id_label = ctk.CTkLabel(self, text="Enter your Student ID:")
        self.student_id_label.pack(pady=10)

        self.student_id_entry = ctk.CTkEntry(self)
        self.student_id_entry.pack(pady=10)

        self.view_gpa_button = ctk.CTkButton(self, text="View GPA", command=self.view_gpa)
        self.view_gpa_button.pack(pady=10)

    def view_gpa(self):
        student_id = self.student_id_entry.get()
        gpa, total_grade_points, total_credits = calculate_cumulative_gpa(student_id)
        default_gpa = get_default_gpa()
        result_text = f"University of Technology\nAcademic Probation Alert GPA Report\n\n"
        result_text += f"Student ID: {student_id}\n"
        result_text += f"Total Grade Points: {total_grade_points:.3f}, Total Credits: {total_credits:.3f}, Cumulative GPA: {gpa:.3f}\n"
        if gpa <= default_gpa:
            result_text += "Status: On Academic Probation\n"
        else:
            result_text += "Status: In Good Standing\n"
        
        # Calculate and display GPA for each semester
        for year in range(2024, 2025):  # Adjust the range as needed
            for semester in range(1, 3):
                semester_gpa, semester_total_grade_points, semester_total_credits = calculate_semester_gpa(student_id, year, semester)
                result_text += f"Year: {year}, Semester: {semester}, GPA: {semester_gpa:.3f}, Total Grade Points: {semester_total_grade_points:.3f}, Total Credits: {semester_total_credits:.3f}\n"
        
        self.result_label = ctk.CTkLabel(self, text=result_text, justify="left")
        self.result_label.pack(pady=20)