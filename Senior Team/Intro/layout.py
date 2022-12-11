from rich.traceback import install
install(show_locals = True)

from rich import print
from rich import box
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout

from datetime import datetime
import keyboard

layout = Layout()

layout.split_column(
    Layout(name = "header", size=3),
    Layout(name = "body"),
    Layout(name = "footer", size=3)
)

layout["body"].split_row(
    Layout(name = "left"),
    Layout(name = "right", ratio = 2)
)

class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Rich[/b] Layout application",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")


def robofunctions():
    funcs = Panel("We used a variety of components in the robot, as well as the majority of the kit given. Cybot comes with the following features:[b red]Speakers[/]for the alarm when in Sentry Mode,[b red]Rigid base[/] and [b red]supporting wheels[/]\nfor improved mobility, [b red]configurable database[/], [b red]translucent body[/]for clear visibility of the interiors, [b red]Camera[/] for video feed,\nand plenty of other aspects.\n\n\nCybot can [b blue]work in tough situations[/] when the building's security is not present. It [b blue]has a performance analysis system[/] for monitoring its health and providing a better picture to the maintenance staff. Cybot [b blue]can operate in a variety of temperatures[/] without difficulty. The robot is [b blue]easily disassembled[/] for maintenance.", title = "Robot features", title_align = "left", box = box.SQUARE, border_style = "bold green")
    
    return funcs



from rich.live import Live
from time import sleep

with Live(layout, refresh_per_second=10, screen=True):
    while True:
        sleep(0.1)
        layout["header"].update(Header())
        layout["left"].update(robofunctions())
        layout["body"].size = 25
        
        
        if keyboard.is_pressed("q"):
            exit()


