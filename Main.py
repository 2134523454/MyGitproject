import tkinter as tk
import pyttsx3
import datetime
import threading  # Import threading for non-blocking text-to-speech
from tkinter import *
from PIL import Image, ImageTk 

# Import pages
from login import create_login_frame
try:
    from second_page import create_second_frame
except ImportError:
    raise ImportError("The module 'second_page' could not be found. Ensure 'second_page.py' exists in the same directory as 'Main.py'.")

# --- Updated speak_text function with threading ---
def speak_text(text):
    def run_tts():
        tts_engine.say(text)
        tts_engine.runAndWait()

    # Run the text-to-speech operation in a separate thread
    tts_thread = threading.Thread(target=run_tts)
    tts_thread.start()

def add_hover_speech(widget, text):
    widget.bind("<Enter>", lambda e: speak_text(text))

def show_frame(frame):
    frame.tkraise()

# --- Init Tkinter ---
root = tk.Tk()
root.title("Voice Bridge")
root.geometry("1180x644")
root.minsize(width=300, height=300)
root.maxsize(width=1180, height=644)
root.config(bg="#b3eaf2") 

# --- Init Text-to-Speech ---
tts_engine = pyttsx3.init()
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = f"audio_log_{timestamp}.mp3"
text = "Default text for audio log"
tts_engine.save_to_file(text, filename)

print(f"Audio log saved as: {filename}")

# --- Frames ---
login_frame = tk.Frame(root, bg="#b3eaf2")
main_frame = tk.Frame(root, bg="#b3eaf2")
second_frame = tk.Frame(root, bg="#b3eaf2")
about_frame = tk.Frame(root, bg="#b3eaf2")

for frame in (login_frame, main_frame, second_frame, about_frame):
    frame.place(relwidth=1, relheight=1)

# --- Setup Pages ---
create_login_frame(login_frame, main_frame, show_frame)
create_second_frame(second_frame, main_frame, speak_text, show_frame)

# --- Main Page Content ---
def setup_main_frame(main_frame, show_frame):
    # Navigation buttons
    home_button = tk.Button(main_frame, text="Home", font=("Arial", 13), bg="black", fg="#00bcd4")
    home_button.place(relx=0.5, rely=0.0, anchor="n")
    
    About_button = tk.Button(main_frame, text="About us", font=("Arial", 13), bg="black", fg="#00bcd4", 
                            command=lambda: show_frame(about_frame))
    About_button.place(relx=0.6, rely=0.0, anchor="n")
    
    contact_button = tk.Button(main_frame, text="Contact us", font=("Arial", 13), bg="black", fg="#00bcd4")
    contact_button.place(relx=0.7, rely=0.0, anchor="n")
    
    Emergancy_button = tk.Button(main_frame, text="Emergancy", font=("Arial", 13), bg="black", fg="#00bcd4")
    Emergancy_button.place(relx=0.8, rely=0.0, anchor="n")
    
    # Header frame
    header_frame = tk.Frame(main_frame, bg="white", width=180, height=90)
    header_frame.place(x=15, y=5)
    header_frame.pack_propagate(False) 
    
    tk.Label(header_frame, text="Voice Bridge ", fg="#004080", bg="white", font=("Arial", 20, "bold")).pack(anchor="n", padx=10)
    tk.Label(header_frame, text="Assistant app", fg="#4a4a4a", bg="white", font=("Arial", 10)).pack(anchor="n", padx=10)
    
    # Main content frame
    new_frame = tk.Frame(main_frame, bg="white", width=800, height=300)
    new_frame.place(relx=0.5, rely=0.4, anchor="center")
    
    new_label = tk.Label(new_frame, text="Voice Bridge", fg="#004080", font=("Arial", 120, "bold"), bg="white")
    new_label.pack(pady=10)
    
    new2_label = tk.Label(new_frame, text="Assistant app", fg="#4a4a4a", font=("Arial", 90, "bold"), bg="white")
    new2_label.pack(pady=10)
    
    # Help button
    Help_button = tk.Button(main_frame, text="Help those who struggle everyday", font=("Arial", 40), bg="black", fg="#00bcd4",
                            command=lambda: show_frame(second_frame))
    Help_button.place(relx=0.5, rely=0.7, anchor="center")

# --- About Page Content ---
def setup_about_frame(about_frame, show_frame):
    about_title = tk.Label(about_frame, text="About Voice Bridge", font=("Arial", 32, "bold"), bg="#b3eaf2", fg="#004080")
    about_title.pack(pady=40)
    
    about_info = tk.Label(
        about_frame,
        text="Voice Bridge is an assistant app designed to help users communicate quickly.\n"
             "Click the buttons to have the app speak preset phrases aloud.\n"
             "You can also log in to save your usage and access more features.",
        font=("Arial", 18),
        bg="#b3eaf2",
        fg="#333333",
        justify="center"
    )
    about_info.pack(pady=20)
    
    about_back = tk.Button(about_frame, text="Back", font=("Arial", 16), bg="black", fg="#00bcd4", 
                          command=lambda: show_frame(main_frame))
    about_back.pack(pady=30)

# Setup the frames
setup_main_frame(main_frame, show_frame)
setup_about_frame(about_frame, show_frame)

# --- Start on login ---
show_frame(login_frame)
root.mainloop() 