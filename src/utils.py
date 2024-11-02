import flet as ft

def add_message(chat_list_view, content, is_user=True, message_container=None):
    if message_container is None:
        container_color = "blue" if is_user else "grey"
        text_color = "white" if is_user else "black"
        alignment = ft.alignment.center_right if is_user else ft.alignment.center_left

        message_container = ft.Container(
            content=ft.Text(content, color=text_color),
            bgcolor=container_color,
            padding=10,
            border_radius=8,
            alignment=alignment,
            expand=True
        )
        chat_list_view.controls.append(message_container)
        chat_list_view.update()
    else:
        message_container.content.value = content
        message_container.update()

    return message_container
