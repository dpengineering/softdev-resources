from dpeaDPi.DPiComputer import DPiComputer
from time import sleep

dpiComputer = DPiComputer()
dpiComputer.initialize()

print("Servo example:")

print("Rotate CW")
servo_number = 0
dpiComputer.writeServo(servo_number, 0)
sleep(3)

print("Rotate CCW")
dpiComputer.writeServo(servo_number, 180)
sleep(3)

print("Recenter")
dpiComputer.writeServo(servo_number, 90)
print("Done")