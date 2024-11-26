import tkinter as tk
from tkinter import messagebox
from student import student_menu
from admin import admin_menu

class UniversityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("University of Technology GPA System")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Are you a student or admin?")
        self.label.pack(pady=10)

        self.student_button = tk.Button(self.root, text="Student", command=self.student_login)
        self.student_button.pack(pady=5)

        self.admin_button = tk.Button(self.root, text="Admin", command=self.admin_login)
        self.admin_button.pack(pady=5)

    def student_login(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Enter your student ID:")
        self.label.pack(pady=10)
        self.student_id_entry = tk.Entry(self.root)
        self.student_id_entry.pack(pady=5)
        self.submit_button = tk.Button(self.root, text="Submit", command=self.student_menu)
        self.submit_button.pack(pady=5)

    def admin_login(self):
        self.clear_screen()
        admin_menu()

    def student_menu(self):
        student_id = self.student_id_entry.get()
        if student_id:
            student_menu(student_id)
        else:
            messagebox.showerror("Error", "Please enter a valid student ID")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversityApp(root)
    root.mainloop()