import tkinter as tk
import subprocess

def start_server():
    # Command to start a simple PHP server
    subprocess.Popen(['php', '-S', 'localhost:8000', '-t', '.'])

# Create the main application window
root = tk.Tk()
root.title("My Application Window")
root.geometry("400x300")

# Create a label widget
label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)

# Create a button to start the server
start_button = tk.Button(root, text="Start HTML and PHP Server", command=start_server)
start_button.pack(pady=10)

# Run the application
root.mainloop()
