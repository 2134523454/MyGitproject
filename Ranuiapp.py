import tkinter as tk
from tkinter import *
import datetime

# Creating the root window 
root = tk.Tk() 
root.title("Ranui App")
root.geometry("1180x644")
root.minsize(width=300, height=300)
root.maxsize(width=1180, height=644) 
root.config(bg="white")

def show_frame(frame):
    frame.tkraise() 

# Allowance dictionary
allowance = {"Nikau": 300, "Hana": 300, "Tia": 300}

# Selected person
selected_person = tk.StringVar(value="")

# Login validation
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        show_frame(main_frame)
    else:
        login_error_label.config(text="Invalid username or password!", fg="red") 

# To display allowance
def show_allowance(person):
    selected_person.set(person)
    allowance_label.config(text=f"{person}'s Allowance: ${allowance[person]}")

# To deduct amount
def deduct_allowance(person, amount):
    if person and allowance[person] >= amount: 
        allowance[person] -= amount
        show_allowance(person)
    else:
        allowance_label.config(text=f"Not enough allowance for {person}!")

# Bonus feature
def check_and_add_bonus(person):
    if person and allowance[person] >= 50:
        allowance[person] += 100
        allowance_label.config(text=f"{person} received a $100 bonus! New Allowance: ${allowance[person]}")
    else:
        allowance_label.config(text=f"{person} does not qualify for a bonus.")

# Login frame
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

# Main frame
main_frame = tk.Frame(root, bg="white")
main_frame.place(relwidth=1, relheight=1)

main_label = tk.Label(main_frame, text="Welcome to the Ranui App!", font=("Arial", 24), bg="white")
main_label.pack(pady=20) 

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

date_label = tk.Label(main_frame, text=f"Date:  {get_current_date()}", font=("Arial", 14), bg="white")
date_label.pack(pady=5) 

# the time label 
time_label = tk.Label(main_frame, text="", font=("Arial", 14), bg="white")
time_label.pack(pady=5)


# the function to update the time 
def update_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")  # Format: Hour:Minute:Second
    time_label.config(text=f"Time: {current_time}")
    main_frame.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

#updating the time 
update_time() 

# Buttons for each person
button_frame = tk.Frame(main_frame, bg="white")
button_frame.pack(pady=20)

for person in allowance.keys():
    person_button = tk.Button(button_frame, text=person, font=("Arial", 14), command=lambda p=person: show_allowance(p))
    person_button.pack(side=tk.LEFT, padx=10)

# Deduction buttons
deduction_frame = tk.Frame(main_frame, bg="white")
deduction_frame.pack(pady=20)

deduct_5_button = tk.Button(deduction_frame, text="Deduct $5", font=("Arial", 14), command=lambda: deduct_allowance(selected_person.get(), 5))
deduct_5_button.pack(side=tk.LEFT, padx=5)

deduct_10_button = tk.Button(deduction_frame, text="Deduct $10", font=("Arial", 14), command=lambda: deduct_allowance(selected_person.get(), 10))
deduct_10_button.pack(side=tk.LEFT, padx=10)

deduct_20_button = tk.Button(deduction_frame, text="Deduct $20", font=("Arial", 14), command=lambda: deduct_allowance(selected_person.get(), 20))
deduct_20_button.pack(side=tk.LEFT, padx=10)

# Allowance label
allowance_label = tk.Label(main_frame, text="Select a person to view allowance", font=("Arial", 14), bg="white")
allowance_label.pack(pady=20)

# Bonus button
bonus_button = tk.Button(main_frame, text="Check Bonus", font=("Arial", 14), command=lambda: check_and_add_bonus(selected_person.get()))
bonus_button.pack(pady=10)

# Raise the login frame initially
login_frame.tkraise()

root.mainloop() 