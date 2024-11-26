import smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'admin@university.com'
    msg['To'] = to

    with smtplib.SMTP('smtp.mailtrap.io', 2525) as server:
        server.login('username', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())

def send_gpa_alert(student, gpa):
    subject = "GPA Alert"
    body = f"Dear {student[1]},\n\nYour current GPA is {gpa}. Please take necessary actions to improve it.\n\nBest regards,\nUniversity Administration"
    send_email(student[2], subject, body)