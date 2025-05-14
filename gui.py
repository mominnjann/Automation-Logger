import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading

stop_flag = threading.Event()

def send_message():
    msg = entry_msg.get()
    try:
        delay = float(entry_delay.get())
        count = int(entry_count.get())
    except ValueError:
        messagebox.showwarning(
            "Input Error",
            "Delay must be a number and count must be an integer."
        )
        return

    if not msg.strip():
        messagebox.showwarning("Input Error", "Please enter a message.")
        return
    if count < 1:
        messagebox.showwarning("Input Error", "Count must be at least 1.")
        return

    stop_flag.clear()

    def automate():
        time.sleep(5)  # Always wait 5 seconds before first message
        for i in range(count):
            if stop_flag.is_set():
                break
            pyautogui.typewrite(msg, interval=0.1)
            pyautogui.press('enter')
            if i < count - 1:
                time.sleep(delay)
        if not stop_flag.is_set():
            messagebox.showinfo("Done", "Messages sent!")

    threading.Thread(target=automate).start()

def stop_message():
    stop_flag.set()

root = tk.Tk()
root.title("Automation Logger - Momin Jan")

# Message input
tk.Label(root, text="Enter your message:").pack(padx=10, pady=(10, 2), anchor="w")
entry_msg = tk.Entry(root, width=40)
entry_msg.pack(padx=10, pady=2, fill="x")

# Delay input
tk.Label(root, text="Delay (seconds):").pack(padx=10, pady=(10, 2), anchor="w")
entry_delay = tk.Entry(root, width=10)
entry_delay.insert(0, "")
entry_delay.pack(padx=10, pady=2, anchor="w")

# Count input
tk.Label(root, text="Count:").pack(padx=10, pady=(10, 2), anchor="w")
entry_count = tk.Entry(root, width=10)
entry_count.insert(0, "")
entry_count.pack(padx=10, pady=2, anchor="w")

# Buttons
frame = tk.Frame(root)
frame.pack(pady=15)
send_btn = tk.Button(frame, text="Send Message", width=15, command=send_message)
send_btn.pack(side=tk.LEFT, padx=10)
stop_btn = tk.Button(frame, text="Stop", width=10, command=stop_message)
stop_btn.pack(side=tk.LEFT, padx=10)

# Info label
tk.Label(
    root,
    text="Switch to your target app before sending. (First message will be sent after 5 seconds)",
    fg="gray"
).pack(padx=10, pady=(5, 15))

root.mainloop()