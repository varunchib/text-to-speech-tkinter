import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
from gtts import gTTS
import os
import platform

engine = pyttsx3.init()

def speak_text():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        engine.stop()
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning('Input Missing', 'Please enter some text to speak')

def save_mp3():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Missing", "Please enter some text to export")
        return

    try:
        tts = gTTS(text=text, lang='en')
        filepath = filedialog.asksaveasfile(defaultextension=".mp3",
                                            filetypes=[("MP# files", "*.mp3")],
                                            title="Save MP# as...")
        if filepath:
            tts.save(filepath)
            messagebox.showinfo("Success", f"Audio saved at:\n{filepath}")

            if platform.system() == 'Windows':
                os.startfile(filepath)
            elif platform.system() == 'Darwin':
                os.system(f"open {filepath}")
            else:
                os.system(f"xdg-open {filepath}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to save MP3: {e}")



# -------------------------- GUI -------------------------- #
app = tk.Tk()
app.title("Text-to-Speech App")
app.geometry("500x400")
app.configure(bg="#f0f4f8")

tk.Label(app, text="Enter your text below:", font=("Arial", 14), bg="#f0f4f8").pack(pady=10)

text_input = tk.Text(app, height=10, font=("Arial", 12), wrap=tk.WORD)
text_input.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(app, bg="#f0f4f8")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Speak (Offline)", command=speak_text, width=20, bg="#007acc", fg="white").grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Export as MP3", command=save_mp3, width=20, bg="#28a745", fg="white").grid(row=0, column=1, padx=10)

app.mainloop()
