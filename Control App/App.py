from rich.panel import Panel
from rich.console import Console
from rich.traceback import install

from rich import box
from rich import print
from rich.table import Table
from rich.layout import Layout

from datetime import datetime
import os
import glob

install(show_locals = True)

layout = Layout()
console = Console()

class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]LOGIC GATE[/b]control application",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")
    
images_path = glob.glob(os.path.join(images_path, "*.*"))

general_info = Panel(f"[b green]Number of Encoded faces in system : {len(images_path)}[/]\n")
    
layout.split_column(
    Layout(name = "header"),
    Layout(name = "body"),
    Layout(name = "footer")
)

layout["body"].split_row(
    Layout(name = "right"),
    Layout(name = "left")
)

layout["right"].split_column(
    Layout(name = "r_upper"),
    Layout(name = "r_lower")
)

layout["header"].size = 3
layout["footer"].size = 3
layout["body"].size = 35

layout["header"].update(Header())

print(layout)