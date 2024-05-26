from diffusers import StableDiffusionPipeline
import torch

class ImageGeneratorModel:
    def __init__(self, model_id="Onodofthenorth/SD_PixelArt_SpriteSheet_Generator"):
        self.model_id = model_id
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_id, torch_dtype=torch.float16)
        self.pipe = self.pipe.to("cuda")

    def generate_image(self, prompt):
        return self.pipe(prompt).images[0]
