import tkinter as tk
import threading
import subprocess
from PIL import Image, ImageTk
 

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Run Python Files")
        self.master.geometry("600x400")
        self.set_background()
        self.create_widgets()

    def create_widgets(self):
        self.file1_button = tk.Button(self.master, text="Game 1", command=self.run_file1, bg="red", fg="white", width=20, height=5, borderwidth=0)
        self.file1_button.grid(row=0, column=0, padx=20, pady=20)

        self.file2_button = tk.Button(self.master, text="Virtual Mouse", command=self.run_file2, bg="green", fg="white", width=20, height=5,borderwidth=0)
        self.file2_button.grid(row=0, column=5, padx=20, pady=20)

        # self.file3_button = tk.Button(self.master, text="File 3", command=self.run_file3, bg="blue", fg="white", width=20, height=5, borderwidth=0)
        # self.file3_button.grid(row=1, column=0, padx=10, pady=10)

        self.file4_button = tk.Button(self.master, text="Media Controller", command=self.run_file4, bg="orange", fg="white", width=20, height=5,borderwidth=0)
        self.file4_button.grid(row=1, column=3, padx=10, pady=10)

        self.status_bar = tk.Label(self.master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="gray", fg="white")
        self.status_bar.grid(row=2, column=0, columnspan=15, sticky=tk.W+tk.E, padx=10, pady=10)

        self.quit_button = tk.Button(self.master, text="Quit!", command=self.master.destroy, bg="black", fg="white", width=10, height=2, borderwidth=0)
        self.quit_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)

    def set_background(self):
        # # Create a canvas widget to hold the background color
        # canvas = tk.Canvas(self.master, width=900, height=700, bg="#34495e")
        # canvas.grid(row=0, column=0, rowspan=4, columnspan=2)
    
    # def set_background(self):
    #     # Load the background image
    #     img = tk.PhotoImage(file="background.png")

    #     # Create a canvas widget to hold the background image
    #     canvas = tk.Canvas(self.master, width=img.width(), height=img.height())
    #     canvas.grid(row=0, column=0, rowspan=4, columnspan=2)

    #     # Set the background image as the canvas background
    #     canvas.create_image(0, 0, image=img, anchor=tk.NW)

        img = Image.open("background1.png")
        img = img.resize((600, 400), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(img)
        self.bg_label = tk.Label(self.master, image=self.bg_image)
        self.bg_label.place(x=0, y=0)


    def run_file(self, file_path):
        self.status_bar.config(text="Running {}".format(file_path))
        subprocess.call(["python", file_path])
        self.status_bar.config(text="")

    def run_file1(self):
        thread = threading.Thread(target=self.run_file, args=("game_1\\main.py",))
        thread.start()

    def run_file2(self):
        thread = threading.Thread(target=self.run_file, args=("virtual_mouse\\geture_controller.py",))
        thread.start()

    # def run_file3(self):
    #     thread = threading.Thread(target=self.run_file, args=("Virtual_click_assisstant\Gesture-Controlled-Virtual-Mouse\src\Proton.py",))
    #     thread.start()

    def run_file4(self):
        thread = threading.Thread(target=self.run_file, args=("media_control\\main.py",))
        thread.start()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
