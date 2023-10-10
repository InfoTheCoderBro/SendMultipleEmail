import tkinter as tk
from tkinter import filedialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to load the first file
def load_file1():
    global file_path1
    file_path1 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

# Function to load the second file
def load_file2():
    global file_path2
    file_path2 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

# Function to load the third file
def load_file3():
    global file_path3
    file_path3 = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

# Function to send emails
def send_emails():
    email_user = email_entry.get()
    email_password = password_entry.get()
    subject = subject_entry.get()

    try:
        # Opening and reading the selected files
        with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2, open(file_path3, 'r') as file3:
            file1_content = file1.read()
            file2_content = file2.readlines()
            file3_content = file3.readlines()

    except FileNotFoundError as e:
        result_label.config(text=f"File not found: {e.filename}")
        return
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")
        return

    message_to_send = file1_content
    friends_names = file2_content
    email_list = file3_content

    # Function to create the email message
    def create_message(friend_name):
        message = f"""Dear {friend_name},
        
{message_to_send}
"""
        return message

    for i, friend_name in enumerate(friends_names):
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_list[i]
        msg['Subject'] = subject

        text = create_message(friend_name.strip())

        msg.attach(MIMEText(text, "plain"))
        text = msg.as_string()

        try:
            # Sending the email using SMTP
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(email_user, email_password)
            server.sendmail(email_user, email_list[i], text)
            result_label.config(text=f"Email sent to {friend_name.strip()}")
            server.quit()
        except Exception as e:
            result_label.config(text=f"An error occurred while sending email to {friend_name.strip()}: {str(e)}")

    result_label.config(text="Finished")

# Create the main application window
app = tk.Tk()
app.title("Email Sender")

# Create and configure widgets
load_button1 = tk.Button(app, text="Load Message File", command=load_file1)
load_button2 = tk.Button(app, text="Load Names File", command=load_file2)
load_button3 = tk.Button(app, text="Load Emails File", command=load_file3)
email_label = tk.Label(app, text="Email:")
email_entry = tk.Entry(app)
password_label = tk.Label(app, text="Password:")
password_entry = tk.Entry(app, show="*")
subject_label = tk.Label(app, text="Subject:")
subject_entry = tk.Entry(app)
send_button = tk.Button(app, text="Send Emails", command=send_emails)
result_label = tk.Label(app, text="")

# Place widgets in the window
load_button1.pack()
load_button2.pack()
load_button3.pack()
email_label.pack()
email_entry.pack()
password_label.pack()
password_entry.pack()
subject_label.pack()
subject_entry.pack()
send_button.pack()
result_label.pack()

app.mainloop()
