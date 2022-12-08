import time
from time import sleep
from rich import box
from rich import print
from rich.console import Console
from rich.panel import Panel

from rich.progress import Progress
from rich.prompt import Prompt, Confirm

from main_video import cam

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

print("""
███████╗ █████╗  ██████╗███████╗    ██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗██╗████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔════╝ ████╗  ██║██║╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗  ███████║██║     █████╗      ██████╔╝█████╗  ██║     ██║   ██║██║  ███╗██╔██╗ ██║██║   ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝  ██╔══██║██║     ██╔══╝      ██╔══██╗██╔══╝  ██║     ██║   ██║██║   ██║██║╚██╗██║██║   ██║   ██║██║   ██║██║╚██╗██║
██║     ██║  ██║╚██████╗███████╗    ██║  ██║███████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                                
""")

import main_video as facerec
facerec.cam()

print(Panel.fit("So that was our [b red]Face recognition system[/] which takes bunch of photos of people and then processes their facial data\nso it can be analyzed and used to detect people.\nIt can work with multiple pictures and without any mistakes as it\nuses a persons facial features and compares it to the\nfaces seen in the camera feed", title = "Explanation", title_align="left", box = box.SQUARE, subtitle=" ... "))

print("""
 █████╗ ██╗      █████╗ ██████╗ ███╗   ███╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
██╔══██╗██║     ██╔══██╗██╔══██╗████╗ ████║    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
███████║██║     ███████║██████╔╝██╔████╔██║    ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
██╔══██║██║     ██╔══██║██╔══██╗██║╚██╔╝██║    ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
██║  ██║███████╗██║  ██║██║  ██║██║ ╚═╝ ██║    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
                                                                                                    
""")
time.sleep(10)

import Alarm_system

print(Panel.fit("That was our [b blue]Alarm System[/] which can be used in places or times when no person is expected or needed. These places could range from vaults to security rooms.\nThis system takes in border reading of different of things in scene and\nthen activates a sound alarm", title = "Explanation", title_align="left", box = box.SQUARE, subtitle=" ... "))
