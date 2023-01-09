from rich.panel import Panel
from rich.layout import Layout
from rich import print

layout = Layout()

layout.split_column(
    Layout(name = "Upper"),
    Layout(name = "body")
    
    )

layout["body"].split(Layout(name = "box1"), Layout(name = "box2"))

def box1():
    1 = Panel("HEY YOU, YEA YOU", border_style = "green")
    return 1

def box2():
    2 = Panel("DONT BE MAD, I WAS TRYING TO HELP", border_style = "red")
    return 2

layout["box1"].update(box1())
layout["box2"].update(box2())

layout["upper"].size = 3

print(layout)