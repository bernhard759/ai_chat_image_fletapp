import flet as ft
from together import Together
from utils import add_message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=api_key, base_url="https://api.together.xyz/v1")

def get_chat_view(page: ft.Page):
    # Create a ListView to hold chat messages
    chat_list_view = ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=True)
    chat_input = ft.TextField(label="Type your message:", width=600)

    def send_chat_message(e):
        # Get user input and clear the text field
        user_message = chat_input.value
        chat_input.value = ""
        chat_input.update()

        # Add the user's message to the chat view
        add_message(chat_list_view, user_message, is_user=True)

        # Placeholder for bot's response
        ai_response_container = add_message(chat_list_view, "", is_user=False)

        # Generate response from Together AI
        stream = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=[{"role": "user", "content": user_message}],
            stream=True,
        )

        # Stream the response from the AI
        ai_message = ""
        for chunk in stream:
            ai_message += chunk.choices[0].delta.content or ""
            # Dynamically update the AI response container as content streams in
            add_message(chat_list_view, ai_message, is_user=False, message_container=ai_response_container)

    def clear_chat(e):
        # Clear all messages in the chat view
        chat_list_view.controls.clear()
        chat_list_view.update()

    # Create buttons for sending and clearing chat
    send_button = ft.ElevatedButton("Send", on_click=send_chat_message)
    clear_button = ft.ElevatedButton("Clear Chat", on_click=clear_chat)

    # Return the chat layout
    return ft.Column(
        [
            ft.Container(content=chat_list_view, height=400, border_radius=8, padding=10, expand=True),
            ft.Row([chat_input, send_button, clear_button], alignment=ft.MainAxisAlignment.CENTER),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )

# Updated add_message function to handle dynamic resizing and light grey background
def add_message(chat_list_view, content, is_user=True, message_container=None):
    """Adds or updates a message in the ListView with appropriate styling."""
    if message_container is None:
        # Determine styles based on whether it's a user or bot message
        container_color = ft.colors.BLUE_200 if is_user else ft.colors.GREY_200
        text_color = "white" if is_user else "black"
        alignment = ft.alignment.center_right if is_user else ft.alignment.center_left

        # Create a new message container
        message_container = ft.Container(
            content=ft.Text(content, color=text_color, expand=True),  # Text expands as content is added
            bgcolor=container_color,
            padding=10,
            border_radius=8,
            alignment=alignment,
            expand=True  # Expand container to fit content
        )

        # Add to chat list view and update
        chat_list_view.controls.append(message_container)
        chat_list_view.update()
    else:
        # Update the existing container with streamed content
        message_container.content.value = content
        message_container.update()

    return message_container
