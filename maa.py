import tkinter as tk
from PIL import Image, ImageTk
import threading
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Run Python Files")
        self.master.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        # Load the background image and display it in a label
        img = Image.open("background.png")
        img = img.resize((600, 400), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(img)
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(x=0, y=0)

        # Create custom button design using an image
        img = Image.open("file1.png")
        img = img.resize((300, 100), Image.ANTIALIAS)
        self.button_image = ImageTk.PhotoImage(img)

        # Create the four buttons with custom design
        self.file1_button = tk.Button(self.master, text="File 1", command=self.run_file1, image=self.button_image, bd=0)
        self.file1_button.place(x=150, y=80)

        self.file2_button = tk.Button(self.master, text="File 2", command=self.run_file2, image=self.button_image, bd=0)
        self.file2_button.place(x=150, y=200)

        self.file3_button = tk.Button(self.master, text="File 3", command=self.run_file3, image=self.button_image, bd=0)
        self.file3_button.place(x=350, y=80)

        self.file4_button = tk.Button(self.master, text="File 4", command=self.run_file4, image=self.button_image, bd=0)
        self.file4_button.place(x=350, y=200)

        # Create the status bar and the quit button
        self.status_bar = tk.Label(self.master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#333333", fg="white")
        self.status_bar.place(x=0, y=370, width=600, height=30)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy, bg="#333333", fg="white", width=10, height=2)
        self.quit_button.place(x=520, y=310)

    def run_file(self, file_path):
        self.status_bar.config(text="Running {}".format(file_path))
        subprocess.call(["python", file_path])
        self.status_bar.config(text="")

    def run_file1(self):
        thread = threading.Thread(target=self.run_file, args=("game_1\\main.py",))
        thread.start()

    def run_file2(self):
        thread = threading.Thread(target=self.run_file, args=("file2.py",))
        thread.start()

    def run_file3(self):
        thread = threading.Thread(target=self.run_file, args=("file3.py",))
        thread.start()

    def run_file4(self):
        thread = threading.Thread(target=self.run_file, args=("file4.py",))
        thread.start()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
