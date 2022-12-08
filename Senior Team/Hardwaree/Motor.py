from time import sleep
from guizero import App, Text, PushButton
from guizero import Robot, LED

motor = Robot(left=(4, 14), right=(17, 18))
motorSwitch = LED(27)

app = App(title = "LOGIC GATE - - MOVEMENT", layout="grid", height=601, width=801)
message = Text(app, text="Dual Motor Control", grid=[4,0])

motorSpeedForward = 0
motorSpeedBackward = 0

def toggle():
    if button0.text == "Start":
        motorSwitch.on()
        button0.text = "Stop"
    elif button0.text == "Stop":
        motorSwitch.off()
        button0.text = "Start"

def Forward_increase():
    global motorSpeedForward
    motor.forward(speed = motorSpeedForward)
    print("Increased motor speed (forward) Current speed = "+ str(motorSpeedForward))
    
    motorSpeedForward += 0.1
    
    if motorSpeedForward >= 1:
        motorSpeedForward = 1
        
        
        
def Forward_decrese():
    global motorSpeedForward
    motor.forward(speed = motorSpeedForward)
    print("Decreased motor speed (forward) Current speed = "+ str(motorSpeedForward))
    
    motorSpeedForward -= 0.1
    
    if motorSpeedForward <= 1:
        motorSpeedForward = 1

def backward_increase():
    global motorSpeedBackward
    motor.forward(speed = motorSpeedBackward)
    print("Increased motor speed (backward) Current speed = "+ str(motorSpeedForward))
    
    motorSpeedForward += 0.1
    
    if motorSpeedForward >= 1:
        motorSpeedForward = 1
        
def backward_decrease():
    global motorSpeedBackward
    motor.forward(speed = motorSpeedBackward)
    print("Increased motor speed (backward) Current speed = "+ str(motorSpeedForward))
    
    motorSpeedForward -= 0.1
    
    if motorSpeedForward <= 1:
        motorSpeedForward = 1
        
Text(app, "Motor", grid=[2, 1])

button0 = PushButton(app, command = toggle(), text="Start", width = 10, height = 3, grid = [2, 4])
button1 = PushButton(app, command = Forward_decrese(), text = "Forward +", width = 10, height = 3, grid = [2, 3])
button2 = PushButton(app, command = Forward_decrese(), text = "Forward -", width = 10, height = 3, grid = [2, 5])
button3 = PushButton(app, command = backward_increase(), text = "Backward +", width = 10, height = 3, grid = [1, 4])
button4 = PushButton(app, command = backward_decrease(), text = "Backward -", width = 10, height = 3, grid = [3, 4])

app.display()