import random
import string
from src.models.image_generator_model import ImageGeneratorModel
from src.views.image_generator_view import ImageGeneratorView

class ImageGeneratorController:
    def __init__(self, root):
        self.model = ImageGeneratorModel()
        self.view = ImageGeneratorView(root, self)

    def generate_image(self):
        prompt = self.view.get_prompt()
        output = self.model.generate_image(prompt)

        filename = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ".png"
        file_output = 'outputs/'+filename
        output.save(file_output)

        self.view.show_image(file_output)

    def open_image(self):
        filename = self.view.ask_open_filename()
        if filename:
            self.view.show_image(filename)