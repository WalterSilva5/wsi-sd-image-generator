import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk#type: ignore

class ImageGeneratorView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        master.title("Image Generator")

        self.prompt_label = tk.Label(master, text="Enter a prompt:")
        self.prompt_label.pack()

        self.prompt_entry = tk.Entry(master)
        self.prompt_entry.pack()

        self.generate_button = tk.Button(master, text="Generate", command=self.controller.generate_image)
        self.generate_button.pack()

        self.open_button = tk.Button(master, text="Open Image", command=self.controller.open_image)
        self.open_button.pack()

        self.panel = None

    def get_prompt(self):
        return self.prompt_entry.get()

    def show_image(self, filename):
        image = Image.open(filename)
        image = image.resize((300, 300))
        photo = ImageTk.PhotoImage(image)

        if self.panel:
            self.panel.destroy()

        self.panel = tk.Label(self.master, image=photo)
        self.panel.image = photo
        self.panel.pack()

    def ask_open_filename(self):
        return filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
