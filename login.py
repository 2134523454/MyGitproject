import tkinter as tk

def create_login_frame(frame, main_frame, show_frame):
    def validate_login():
        username = username_entry.get()
        password = password_entry.get()
        if username == "DDT123" and password == "DDT123":
            try:
                with open("records.txt", "a") as f:
                    f.write(f"{username}, {password},\n")
            except FileNotFoundError as e:
                print(f"Error: {e}")
            show_frame(main_frame)
        else:
            login_error_label.config(text="Invalid username or password!", fg="red")

    # --- Widgets ---
    tk.Label(frame, text="Login", font=("Arial", 24), bg="#b3eaf2").pack(pady=20)

    tk.Label(frame, text="Username:", font=("Arial", 14), bg="#b3eaf2").pack(pady=5)
    username_entry = tk.Entry(frame, font=("Arial", 14))
    username_entry.pack(pady=5)

    tk.Label(frame, text="Password:", font=("Arial", 14), bg="#b3eaf2").pack(pady=5)
    password_entry = tk.Entry(frame, font=("Arial", 14), show="*")
    password_entry.pack(pady=5)

    login_button = tk.Button(frame, text="Login", font=("Arial", 14), command=validate_login)
    login_button.pack(pady=20)

    login_error_label = tk.Label(frame, text="", font=("Arial", 12), bg="#b3eaf2")
    login_error_label.pack()