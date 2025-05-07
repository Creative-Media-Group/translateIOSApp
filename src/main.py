import flet as ft
from new import localisation


def main(page: ft.Page):
    mytext = ft.Text(value=localisation())
    page.add(
        ft.SafeArea(
            ft.Container(
                mytext,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
