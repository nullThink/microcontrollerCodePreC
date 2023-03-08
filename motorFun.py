import machine
import time
from motorController import *

board = NanoMotorBoard()
board.reboot()

motor = DCMotor(0)
b = motor.setDuty(0)
b = motor.resetEncoder(0)


b = motor.resetEncoder(0)
b = motor.setDuty(30)
time.sleep(1)
b = motor.setDuty(0)
time.sleep(1)