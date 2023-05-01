import tkinter as tk
from tkinter import ttk
import os
import threading
import subprocess

class App:
    def __init__(self, master):
        self.master = master
        master.title("Python File Runner")
        master.geometry("800x600")

        # Set up the background image
        self.background_image = tk.PhotoImage(file="background.png")
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Set up the heading
        self.heading = ttk.Label(master, text="Select a HandGesture Function to do:", font=("Helvetica", 18))
        self.heading.pack(pady=20)

        # Set up the buttons
        self.button1 = ttk.Button(master, text="File 1", command=self.run_file1)
        self.button1.pack(side="left", padx=55, pady=30)
        self.button1_image = tk.PhotoImage(file="file1.png")
        self.button1.config(image=self.button1_image, compound="top")

        self.button2 = ttk.Button(master, text="File 2", command=self.run_file2)
        self.button2.pack(side="left", padx=40, pady=30)
        self.button2_image = tk.PhotoImage(file="file2.png")
        self.button2.config(image=self.button2_image, compound="top")

        self.button3 = ttk.Button(master, text="File 3", command=self.run_file3)
        self.button3.pack(side="left", padx=40, pady=30)
        self.button3_image = tk.PhotoImage(file="file3.png")
        self.button3.config(image=self.button3_image, compound="top")

        self.button4 = ttk.Button(master, text="File 4", command=self.run_file4)
        self.button4.pack(side="left", padx=40, pady=30)
        self.button4_image = tk.PhotoImage(file="file2.png")
        self.button4.config(image=self.button4_image, compound="top")

        # Set up the quit button
        self.quit_button = ttk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(side="bottom", pady=20)

    def run_file(self, file_path):
        subprocess.call(["python", file_path])

    def run_file1(self):
        thread = threading.Thread(target=self.run_file, args=("game_1\\main.py",))
        thread.start()

    def run_file2(self):
        thread = threading.Thread(target=self.run_file, args=("media_control\\main.py",))
        thread.start()

    def run_file3(self):
        thread = threading.Thread(target=self.run_file, args=("virtual_mouse\\geture_controller.py",))
        thread.start()

    def run_file4(self):
        thread = threading.Thread(target=self.run_file, args=("file4.py",))
        thread.start()

root = tk.Tk()
app = App(root)
root.mainloop()
