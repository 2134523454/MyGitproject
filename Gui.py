import tkinter as tk
from tkinter import *

root = tk.Tk() 
root.title("Voice Bridge")
root.geometry("1180x644")
root.minsize(width=300, height=300)
root.maxsize(width=1180, height=644) 
root.config(bg="white") 

# Warning! Represents a warning that needs attention.
# "Danger!" Represents a dangerous negative action.
# Success 

# Main frame

def hide_welcome_message():
    main_label.pack_forget() 
def show_frame(frame):
    frame.tkraise()
main_frame = tk.Frame(root, bg="white")
main_frame.place(relwidth=1, relheight=1) 
main_frame.place(relx=1.0, rely=0.0, anchor="ne")

menu_bar = tk.Menu(main_frame) 

main_label = tk.Label(main_frame, text="Welcome to Voice Bridge", font=("Arial",20), bg="white")
main_label.pack(pady=20)

# Login validation
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        show_frame(main_frame)
    else:
        login_error_label.config(text="Invalid username or password!", fg="red") 

login_frame = tk.Frame(root, bg="white")
login_frame.place(relwidth=1, relheight=1)

login_label = tk.Label(login_frame, text="Login", font=("Arial", 24), bg="white")
login_label.pack(pady=20)

username_label = tk.Label(login_frame, text="Username:", font=("Arial", 14), bg="white")
username_label.pack(pady=5)
username_entry = tk.Entry(login_frame, font=("Arial", 14))
username_entry.pack(pady=5)

password_label = tk.Label(login_frame, text="Password:", font=("Arial", 14), bg="white")
password_label.pack(pady=5)
password_entry = tk.Entry(login_frame, font=("Arial", 14), show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", font=("Arial", 14), command=validate_login)
login_button.pack(pady=20)

login_error_label = tk.Label(login_frame, text="", font=("Arial", 12), bg="white")
login_error_label.pack() 

root.after(8000, hide_welcome_message) 
root.mainloop() 