import flet as ft
from remove_limit import unlimit
from notify import Notify
from dataclasses import dataclass

@dataclass
class GlobalClass:
    tool_name: str = "CatelliteV2F"

global_context = ft.create_context(GlobalClass())

@ft.component
def App():
    gc = ft.use_context(global_context)
    def unlock(e):
        result = unlimit(gc.tool_name)
        match result:
            case 1:
                Notify("ソース側でツール名が指定されていないため\n制限解除できませんでした。", ft.Colors.RED)
            case 2:
                Notify(f"{gc.tool_name}が一度も実行されていないため\n制限解除できませんでした。", ft.Colors.RED)
            case _:
                Notify(f"{gc.tool_name}の制限を解除しました！", ft.Colors.GREEN)

    return ft.Column([
        ft.Container(
            content=ft.Text(
                f"ご購入ありがとうございます！\n本ツールでは以下のレジストリを書き換えます。\nあらかじめご了承ください。\nSoftware\\{gc.tool_name}\n以下の制限解除ボタンを押すことで\nツールのトライアル制限が解除されます。"
            ),
            alignment=ft.Alignment.CENTER,
            expand=True
        ),
        ft.Button(
            "制限解除！",
            icon=ft.Icons.LOCK_OPEN,
            expand=True,
            on_click=unlock
        )
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)

def main(page: ft.Page):
    page.title = f"{GlobalClass.tool_name} Unlimitor"
    page.window.width = 400
    page.window.height = 400
    page.window.resizable = False
    page.window.maximizable = False

    page.render(App)


ft.run(main)
