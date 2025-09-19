import pyttsx3

# Initialize TTS engine once
_tts_engine = pyttsx3.init()

def speak_text(text: str):
    """Speaks the given text using TTS."""
    _tts_engine.say(text)
    _tts_engine.runAndWait()

def save_audio_log(text: str, filename: str):
    """Saves spoken text as an audio file."""
    _tts_engine.save_to_file(text, filename)
    _tts_engine.runAndWait()

def add_hover_speech(widget, text: str):
    """Makes a widget speak when hovered over."""
    widget.bind("<Enter>", lambda e: speak_text(text)) 

    