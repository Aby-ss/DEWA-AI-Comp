import RPi.GPIO as GPIO 
from time import sleep
# Pins for Motor Driver Inputs
MotorlA = 4
Motor1B = 5

def setup():


    GPIO.setwarnings (False)

    GPIO. setmode (GPIO. BCM)

    GPIO. setup (MotorIA, GPIO.OUT)

    GPIO. setup (Motor1B, GPIO. OUT)
def loop ():
    # Going forwards
    GPIO.output (MotorlA, GPIO. HIGH)
    GPIO.output (MotorIB, GPIO.HIGH)
    print ("Going forwards")
    sleep (5)
    
# Stop
GPIO.output (MotorlA, GPIO. LOW)
GPIO.output (MotorIB, GPIO.LOW)
print ("Stop")

def destroy ():
    GPIO. cleanup ()
if __name__ == "__main__":
    setup()
    try : 
            loop()
    except KeyboardInterrupt:
        destroy()