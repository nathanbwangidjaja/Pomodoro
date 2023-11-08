import tkinter as tk
from tkinter import messagebox

# Constants for the Pomodoro Timer
POMODORO_TIME = 25 * 60  # 25 minutes
SHORT_BREAK = 5 * 60     # 5 minutes
LONG_BREAK = 15 * 60     # 15 minutes
REPEATS = 4              # Number of pomodoros before a long break

# Tkinter setup for GUI
root = tk.Tk()
root.title("Pomodoro Timer")

# Initialize variables
timer = None
repeats = 0
timer_running = False
time_left = POMODORO_TIME

# Function to update the global variable
def set_timer_running(run):
    global timer_running
    timer_running = run

# Function to start the timer
def start_timer():
    global repeats, time_left
    if not timer_running:
        set_timer_running(True)
        pause_button.config(text="Pause")  # Ensure the button says "Pause"
        repeats += 1
        if repeats % (REPEATS + 1) == 0:
            time_left = LONG_BREAK
            messagebox.showinfo("Break", "Long break!")
        elif repeats % 2 == 0:
            time_left = SHORT_BREAK
            messagebox.showinfo("Break", "Short break!")
        else:
            time_left = POMODORO_TIME
            messagebox.showinfo("Work", "Time to work!")
        countdown(time_left)

# Function to countdown
def countdown(count):
    global timer, time_left
    time_left = count
    minutes, seconds = divmod(count, 60)
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    if count > 0 and timer_running:
        timer = root.after(1000, countdown, count - 1)
    else:
        set_timer_running(False)
        time_left = POMODORO_TIME  # Reset time_left when the timer is not running

# Function to reset the timer
def reset_timer():
    global timer, time_left, repeats
    if timer:
        root.after_cancel(timer)
    timer_label.config(text="25:00")
    set_timer_running(False)
    pause_button.config(text="Pause")  # Reset the pause button to say "Pause"
    time_left = POMODORO_TIME
    repeats = 0

# Function to pause or resume the timer
def pause_or_resume_timer():
    global timer_running
    if timer_running:
        root.after_cancel(timer)
        set_timer_running(False)
        pause_button.config(text="Resume")  # Change the button to say "Resume"
    else:
        set_timer_running(True)
        pause_button.config(text="Pause")  # Change the button back to say "Pause"
        countdown(time_left)  # Continue the countdown from where it was paused

# Layout
timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
timer_label.pack()

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

pause_button = tk.Button(root, text="Pause", command=pause_or_resume_timer)
pause_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_timer)
reset_button.pack()

# Start the GUI
root.mainloop()
