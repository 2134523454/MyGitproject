import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Voice Bridge")
root.geometry("1180x644")
root.minsize(width=300, height=300)
root.maxsize(width=1180, height=644)
root.config(bg="#968ce4")

# Frame Management 
def show_frame(frame):
    frame.tkraise()

login_frame = tk.Frame(root, bg="#968ce4")
main_frame = tk.Frame(root, bg="#968ce4")
second_frame = tk.Frame(root, bg="#968ce4")

for frame in (login_frame, main_frame, second_frame):
    frame.place(relwidth=1, relheight=1)

#Login Page
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "ab" and password == "ab":
        try:
            with open("records.txt", "a") as f:
                f.write(f"{username}, {password},\n")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        show_frame(main_frame)
    else:
        login_error_label.config(text="Invalid username or password!", fg="red")

login_label = tk.Label(login_frame, text="Login", font=("Arial", 24), bg="#968ce4")
login_label.pack(pady=20)

username_label = tk.Label(login_frame, text="Username:", font=("Arial", 14), bg="#968ce4")
username_label.pack(pady=5)
username_entry = tk.Entry(login_frame, font=("Arial", 14))
username_entry.pack(pady=5)

password_label = tk.Label(login_frame, text="Password:", font=("Arial", 14), bg="#968ce4")
password_label.pack(pady=5)
password_entry = tk.Entry(login_frame, font=("Arial", 14), show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", font=("Arial", 14), command=validate_login)
login_button.pack(pady=20)

login_error_label = tk.Label(login_frame, text="", font=("Arial", 12), bg="#968ce4")
login_error_label.pack()

# Main Frame 
home_button = tk.Button(main_frame, text="Home", font=("Arial", 13), bg="black", fg="#f7b8d2")
home_button.place(relx=0.5, rely=0.0, anchor="n")

About_button = tk.Button(main_frame, text="About us", font=("Arial", 13), bg="black", fg="#f7b8d2")
About_button.place(relx=0.6, rely=0.0, anchor="n")

contact_button = tk.Button(main_frame, text="Contact us", font=("Arial", 13), bg="black", fg="#f7b8d2")
contact_button.place(relx=0.7, rely=0.0, anchor="n")

service_button = tk.Button(main_frame, text="Service", font=("Arial", 13), bg="black", fg="#f7b8d2")
service_button.place(relx=0.8, rely=0.0, anchor="n")

header_frame = tk.Frame(main_frame, bg="white", width=180, height=90)
header_frame.place(x=15, y=5)
header_frame.pack_propagate(False)

tk.Label(header_frame, text="Voice Bridge ", fg="#6b64b8", bg="white", font=("Arial", 20, "bold")).pack(anchor="n", padx=10)
tk.Label(header_frame, text="Assistant app", fg="#2b2a2a", bg="white", font=("Arial", 10)).pack(anchor="n", padx=10)

new_frame = tk.Frame(main_frame, bg="white", width=800, height=300)
new_frame.place(relx=0.5, rely=0.4, anchor="center")

new_label = tk.Label(new_frame, text="Voice Bridge", fg="#6b64b8", font=("Arial", 120, "bold"), bg="white")
new_label.pack(pady=10)

new2_label = tk.Label(new_frame, text="Assistant app", fg="#737373", font=("Arial", 90, "bold"), bg="white")
new2_label.pack(pady=10)

Help_button = tk.Button(main_frame, text="Help those who struggle everyday", font=("Arial", 40), bg="black", fg="#f7b8d2",
                        command=lambda: show_frame(second_frame))
Help_button.place(relx=0.5, rely=0.7, anchor="center")

# Second Page Frame with Button 

second_label = tk.Label(second_frame, text="Communication Buttons", font=("Arial", 35, "bold"), bg="#968ce4", fg="white")
second_label.pack(pady=20)

# Frame positions
top_left_frame = tk.Frame(second_frame, bg="white", width=500, height=300)
top_left_frame.place(x=0, y=80)

top_right_frame = tk.Frame(second_frame, bg="white", width=500, height=300)
top_right_frame.place(x=590, y=80)

bottom_left_frame = tk.Frame(second_frame, bg="white", width=500, height=300)
bottom_left_frame.place(x=0, y=390)

bottom_right_frame = tk.Frame(second_frame, bg="white", width=500, height=300)
bottom_right_frame.place(x=590, y=390)

# Buttons inside frames
option_1_button = tk.Button(top_left_frame, text="Can I go to the bathroom", font=("Arial", 25), bg="black", fg="pink")
option_1_button.place(relx=0.5, rely=0.1, anchor="n")

option_2_button = tk.Button(top_right_frame, text="I wanna go outside", font=("Arial", 25), bg="black", fg="pink")
option_2_button.place(relx=0.5, rely=0.1, anchor="n")

option_3_button = tk.Button(bottom_left_frame, text="I want to watch TV", font=("Arial", 25), bg="black", fg="pink")
option_3_button.place(relx=0.5, rely=0.1, anchor="n")

option_4_button = tk.Button(bottom_right_frame, text="I'm hungry", font=("Arial", 25), bg="black", fg="pink")
option_4_button.place(relx=0.5, rely=0.1, anchor="n")

# Back button
back_button = tk.Button(second_frame, text="Back to Home", font=("Arial", 20), bg="black", fg="#f7b8d2",
                        command=lambda: show_frame(main_frame))
back_button.place(relx=0.5, rely=0.95, anchor="s")

# Start App on Login Page 
show_frame(login_frame)
root.mainloop() 