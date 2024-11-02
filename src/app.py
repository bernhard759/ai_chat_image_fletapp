import flet as ft
from chat_page import get_chat_view
from image_generator_page import get_image_generator_view

def main(page: ft.Page):
    page.title = "Together AI Chat and Image App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Create Tabs
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Chat", content=get_chat_view(page)),
            ft.Tab(text="Image Generator", content=get_image_generator_view(page)),
        ],
        expand=True,
    )

    # Add Tabs to the page
    page.add(tabs)
    page.update()

# Run Flet app
ft.app(target=main)
