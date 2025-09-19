import tkinter as tk

def create_second_frame(frame, main_frame, speak_text, show_frame):
    # Top frames
    top_left_frame = tk.Frame(frame, bg="white", width=700, height=200)
    top_left_frame.place(x=0, y=80)

    top_right_frame = tk.Frame(frame, bg="white", width=700, height=200)
    top_right_frame.place(x=590, y=80)

    bottom_left_frame = tk.Frame(frame, bg="white", width=700, height=200)
    bottom_left_frame.place(x=0, y=390)

    bottom_right_frame = tk.Frame(frame, bg="white", width=700, height=200)
    bottom_right_frame.place(x=590, y=390)

    # Buttons
    tk.Button(top_left_frame, text="Can I go to the bathroom", font=("Arial", 45),
              bg="black", fg="#00bcd4",
              command=lambda: speak_text("Can I go to the bathroom")).place(relx=0.5, rely=0.1, anchor="n")

    tk.Button(top_right_frame, text="I wanna go outside", font=("Arial", 45),
              bg="black", fg="#00bcd4",
              command=lambda: speak_text("I wanna go outside")).place(relx=0.5, rely=0.1, anchor="n")

    tk.Button(bottom_left_frame, text="I want to watch TV", font=("Arial", 45),
              bg="black", fg="#00bcd4",
              command=lambda: speak_text("I want to watch TV")).place(relx=0.5, rely=0.1, anchor="n")

    tk.Button(bottom_right_frame, text="I'm hungry", font=("Arial", 45),
              bg="black", fg="#00bcd4",
              command=lambda: speak_text("I'm hungry")).place(relx=0.5, rely=0.1, anchor="n")

    # Back button
    tk.Button(frame, text="Back to Home", font=("Arial", 20),
              bg="black", fg="#00bcd4",
              command=lambda: show_frame(main_frame)).place(relx=0.5, rely=0.95, anchor="s")