from diffusers import DiffusionPipeline
import matplotlib.pyplot as plt

def generate_img(prompt, num_reference=1):
    pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
    pipe = pipe.to("mps") # m1 pro gpu option

    # Recommended if your computer has < 64 GB of RAM
    pipe.enable_attention_slicing()

    # First-time "warmup" pass if PyTorch version is 1.13 (see explanation above)
    _ = pipe(prompt, num_inference_steps=num_reference)

    # Results match those from the CPU device after the warmup pass.
    image = pipe(prompt).images[0]

    return image
    # generate_img("아주 옛날에 사랑받는 작고 귀여운 소녀가 있었습니다.")