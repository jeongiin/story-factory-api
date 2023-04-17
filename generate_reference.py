from diffusers import DiffusionPipeline
import matplotlib.pyplot as plt
import io
import base64
from PIL import Image


def img2bytes(img):
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return encoded_img

def generate_img(prompt, txt2img):
    pipe = DiffusionPipeline.from_pretrained(txt2img.model_diff)
    pipe = pipe.to("mps") # m1 pro gpu option

    # Recommended if your computer has < 64 GB of RAM
    pipe.enable_attention_slicing()

    # First-time "warmup" pass if PyTorch version is 1.13 (see explanation above)
    # _ = pipe(prompt)

    # Results match those from the CPU device after the warmup pass.
    image = pipe(prompt=prompt, height=txt2img.height, width=txt2img.width,
                 num_inference_steps=txt2img.num_inference_steps, 
                num_images_per_prompt=txt2img.number_of_imgs).images   

    return image
