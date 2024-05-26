from src.controllers.image_generator_controller import ImageGeneratorController
import tkinter as tk

def main():
    root = tk.Tk()
    _app = ImageGeneratorController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
