import flet as ft

def Notify(msg: str, color: ft.Colors):
    page = ft.context.page
    page.show_dialog(
        ft.SnackBar(
            ft.Text(msg, text_align=ft.TextAlign.START, weight=ft.FontWeight.BOLD),
            bgcolor=color,
            behavior=ft.SnackBarBehavior.FLOATING,
            margin=ft.Margin(top=10, bottom=280),
            duration=2000,
        )
    )