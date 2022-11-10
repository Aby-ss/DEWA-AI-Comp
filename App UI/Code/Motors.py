from rich import print
from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

from time import sleep
from guizero import App, Text, PushButton
from gpiozero import Robot, LED


motor = Robot(left=(4, 14), right=(17, 18))
motorSwitch= LED(27)

forward = 0
backward = 0

console = Console()

def forward_increase():
    global motorSpeedForward
    motor.forward(speed=motorSpeedForward)
    console.log(Panel("Increased speed of motor backward. Current speed = "+ str(motorSpeedForward), title = "Motor Values", title_align = "left", box = box.SQUARE, border_style = "bold green", subtitle = "  ...  "))
    motorSpeedForward += 0.1
    if motorSpeedForward >= 1:
        motorSpeedForward = 1
    
def forwardSpeedReduce():
    global motorSpeedForward
    motor.forward(speed=motorSpeedForward)
    console.log(Panel("Reduce speed of motor forward. Current speed = "+ str(motorSpeedForward), title = "Motor Values", title_align = "left", box = box.SQUARE, border_style = "bold green", subtitle = "  ...  "))
    motorSpeedForward -= 0.1
    if motorSpeedForward <= 0:
        motorSpeedForward = 0

def backwardSpeedIncrease():
    global motorSpeedBackward
    motor.forward(speed=motorSpeedBackward)
    console.log(Panel("Increased speed of motor backward. Current speed = "+ str(motorSpeedBackward), title = "Motor Values", title_align = "left", box = box.SQUARE, border_style = "bold green", subtitle = "  ...  "))
    motorSpeedBackward += 0.1
    if motorSpeedBackward >= 1:
        motorSpeedBackward = 1

def backwardSpeedReduce():
    global motorSpeedBackward
    motor.backward(speed=motorSpeedBackward)
    console.log(Panel("Reduce speed of motor backward. Current speed = "+ str(motorSpeedBackward), title = "Motor Values", title_align = "left", box = box.SQUARE, border_style = "bold green", subtitle = "  ...  "))
    motorSpeedBackward -= 0.1
    if motorSpeedBackward <= 0:
        motorSpeedBackward = 0

