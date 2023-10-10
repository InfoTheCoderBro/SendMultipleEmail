# SendMultipleEmail
This Python script uses the tkinter library to create a graphical user interface (GUI) application for sending emails to a list of recipients. 

Here's a description of the script's main functionality and components:

Importing Libraries:

The script starts by importing the necessary libraries, including tkinter for creating the GUI, filedialog for file selection dialogs, smtplib for sending emails, and modules for creating email content.
File Loading Functions:

There are three functions (load_file1, load_file2, and load_file3) defined to load three different text files. These files are selected using file dialogs and are expected to contain the message content, recipient names, and email addresses, respectively.
Send Emails Function (send_emails):

This function is responsible for sending emails to the recipients. It first retrieves the email user, email password, and email subject from the corresponding entry fields in the GUI.
It then attempts to open and read the three selected files, capturing their content.
Next, it iterates over the list of recipient names, creates personalized email messages using the message content and recipient names, and sends these messages to the corresponding email addresses.
The results of each email sending attempt are displayed in the result_label.
Create Message Function (create_message):

This nested function is used within the send_emails function to create individualized email messages for each recipient. It takes the recipient's name as input and combines it with the main message content.
Main Application Window (app):

The main GUI window is created using tk.Tk(), and its title is set to "Email Sender."
Widgets:

Several widgets are created for interacting with the user:
Buttons (load_button1, load_button2, load_button3) for loading the message content, recipient names, and email addresses files.
Labels (email_label, password_label, subject_label) and entry fields (email_entry, password_entry, subject_entry) for inputting email-related information.
A "Send Emails" button (send_button) to trigger the email sending process.
A label (result_label) for displaying the results of email sending.
Widget Placement:

Widgets are packed within the main window, specifying their positions and layout in the GUI.
Main Loop (app.mainloop()):

The script enters the tkinter main event loop, allowing the user to interact with the GUI and trigger actions such as loading files and sending emails.
Overall, this script provides a user-friendly interface for sending personalized emails to a list of recipients, where the message content, recipient names, and email addresses can be loaded from separate text files. The email configuration and results are displayed within the same GUI.





