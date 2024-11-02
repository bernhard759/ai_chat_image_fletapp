import flet as ft
from together import Together
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=api_key, base_url="https://api.together.xyz/v1")

def get_image_generator_view(page: ft.Page):
    image_prompt = ft.TextField(label="Describe the image you want:", width=600)
    image_output = ft.Image(width=400, height=400, visible=False)
    loading_indicator = ft.Container(content=ft.ProgressRing(), visible=False, alignment=ft.alignment.center, width=400, height=400)

    def generate_image(e):
        prompt = image_prompt.value
        model = "black-forest-labs/FLUX.1-schnell-Free"
        loading_indicator.visible = True
        image_output.visible = False
        page.update()

        try:
            response = client.images.generate(prompt=prompt, model=model, steps=2, n=1)
            if response.data and response.data[0].url:
                image_output.src = response.data[0].url
                image_output.visible = True
            else:
                print("No image data found in response.")
        except Exception as error:
            print("Error generating image:", error)

        loading_indicator.visible = False
        page.update()

    generate_button = ft.ElevatedButton("Generate Image", on_click=generate_image)

    return ft.Column(
    [
        # Wrap loading_indicator in a container with centered alignment
        ft.Container(content=loading_indicator, alignment=ft.alignment.center),
        
        # Wrap image_output in a container with centered alignment
        ft.Container(content=image_output, alignment=ft.alignment.center),

        # Horizontal space added here
        ft.Container(height=20),

        # Center the row with the prompt and button
        ft.Row([image_prompt, generate_button], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
    ],
    alignment=ft.MainAxisAlignment.CENTER,  # Center align the entire column
    spacing=10,
)
