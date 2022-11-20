import flet
from flet import (
    Page,
    Row,
    icons,
    IconButton,
    TextField
)

def main(page: Page):
    page.title = "counter"
    page.vertical_alignment = "center"

    num = TextField(value='0', text_align="right", width=100)

    def minus_click(e):
        num.value = int(num.value)-1
        page.update()

    def plus_click(e):
        num.value = int(num.value)+1
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                num,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center"
        )
    )

flet.app(target=main)
    