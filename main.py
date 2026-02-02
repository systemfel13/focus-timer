import tkinter as tk # GUI
from plyer import notification 
from PIL import Image, ImageTk # PIL/Pillow: library to work with pictures

class FocusTimer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Focus Timer")
        self.window.geometry("700x500")
        self.window.configure(bg="#FFB6C1")

        self.time_left = 1800 # 1800 seconds = 30 minutes 
        self.total_time = 1800

        # Spacer to move everything down
        spacer = tk.Label(self.window, bg="#FFB6C1", height=8) # Higher number on height moves everything down more
        spacer.pack() # pack: tkinters layout manager, decides where widgets is placed in the window

        self.time_label = tk.Label(
            self.window, 
            text="30:00", 
            font=("Century Gothic", 72, "bold"),
            bg="#FFB6C1",
            fg="white"
        )
        self.time_label.pack() # Place the label in the window

        # Button
        self.button = tk.Button(
            self.window, 
            text="Start work session", 
            command=self.start_timer,
            font=("Century Gothic", 16, "bold"),
            bg="white",
            fg="#FFB6C1",
            padx=30, # Makes the button wider
            pady=15, # Space in the button above/under the text
            relief="flat", # Makes the button flat
            cursor="hand2" # The cursors becomes a and when it's over the button
        )
        self.button.pack(pady=20) # Place the button in the window, pady=20 is space around the button

    def start_timer(self):
        self.countdown()

    def countdown(self):
        if self.time_left > 0:
            # Mathematic operations to get minutes:seconds format
            mins = self.time_left // 60
            secs = self.time_left % 60
            self.time_label.config(text=f"{mins}:{secs:02d}") # 02d: show as a decimal with two numbers. Eg mins = 1, secs = 5, without 02d = 1:5, with = 1:05
            self.time_left -= 1
            self.window.after(1000, self.countdown)
        else:
            self.break_notification()

    def break_notification(self):
        notification.notify(
            title="Break time",
            message="You've worked for 30 minutes, time to take a break!",
            timeout=20
        )

timer = FocusTimer()
timer.window.mainloop()