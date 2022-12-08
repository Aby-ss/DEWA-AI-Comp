import time
from time import sleep
from rich import box
from rich import print
from rich.console import Console
from rich.panel import Panel

from rich.progress import Progress
from rich.prompt import Prompt, Confirm



console = Console()

print("""
██╗      ██████╗  ██████╗ ██╗ ██████╗     ██████╗  █████╗ ████████╗███████╗
██║     ██╔═══██╗██╔════╝ ██║██╔════╝    ██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝
██║     ██║   ██║██║  ███╗██║██║         ██║  ███╗███████║   ██║   █████╗  
██║     ██║   ██║██║   ██║██║██║         ██║   ██║██╔══██║   ██║   ██╔══╝  
███████╗╚██████╔╝╚██████╔╝██║╚██████╗    ╚██████╔╝██║  ██║   ██║   ███████╗
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
""")

print(Panel.fit("[b red]WELCOME[/] to the software presentation of [b purple]LOGIC GATE[/]. You will get familirized with the software and also get a \ntutorial on how to operate the system. \n       [b blue]So lets get started !", title = ". . .", title_align = "left", subtitle = "LOGIC GATE", subtitle_align = "left"))


with Progress() as progress:

    task1 = progress.add_task("[red]Setting up system...", total=1000)
    task2 = progress.add_task("[green]Processing Database...", total=1000)
    task3 = progress.add_task("[cyan]Checking hardware...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=0.8)
        progress.update(task2, advance=0.7)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)
        
print(Panel.fit("[b green]CENTRAL PROCESSING COMPLETE[/]", border_style = "b green"))

is_rich_great = Confirm.ask("Start Tour?")
assert is_rich_great

