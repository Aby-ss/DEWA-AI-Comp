from rich import box
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.progress import Progress
from rich.prompt import Prompt, Confirm

import keyboard

from time import sleep

console = Console()


print("""
███████╗███╗   ███╗ █████╗ ███████╗██╗  ██╗     ██████╗██╗      █████╗ ███╗   ██╗
██╔════╝████╗ ████║██╔══██╗██╔════╝██║  ██║    ██╔════╝██║     ██╔══██╗████╗  ██║
███████╗██╔████╔██║███████║███████╗███████║    ██║     ██║     ███████║██╔██╗ ██║
╚════██║██║╚██╔╝██║██╔══██║╚════██║██╔══██║    ██║     ██║     ██╔══██║██║╚██╗██║
███████║██║ ╚═╝ ██║██║  ██║███████║██║  ██║    ╚██████╗███████╗██║  ██║██║ ╚████║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝      
""")

print(Panel.fit("[b red]WELCOME[/] to the software presentation of [b blue]SMASH CLAN[/]. You will get familirized with the software and also get a \ntutorial on how to operate the system. \n       [b red]So lets get started !", title = ". . .", title_align = "left", subtitle = "SMASH CLAN", subtitle_align = "left"))


is_rich_great = Confirm.ask("Start Tour?")
assert is_rich_great

print("""
███████╗██████╗  ██████╗ ███████╗    ██████╗ ███████╗████████╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔══██╗██╔════╝ ██╔════╝    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
█████╗  ██║  ██║██║  ███╗█████╗      ██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║
██╔══╝  ██║  ██║██║   ██║██╔══╝      ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║
███████╗██████╔╝╚██████╔╝███████╗    ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝╚═════╝  ╚═════╝ ╚══════╝    ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝      
""")

import Edge_detect as ed


print(Panel.fit("[b red]The Edge Detection[/] feature detects all the edges of any surface shown on the camera feed and processes them into a black and white video format so we can\neasily spot any uneven surfaces or cracks.\nThe system then saves a recording of this footage which can be analyzed by the staff.", title = "Explanation", title_align="left", box = box.SQUARE, subtitle=" ... "))

sleep(15)


if keyboard.is_pressed("q"):
    exit()
