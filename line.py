#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, GyroSensor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Button, Direction, Stop, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
import math

# Init
brick = EV3Brick()
color = ColorSensor(Port.S4)
l_motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
r_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)
s_motor = Motor(Port.B)
base = DriveBase(l_motor, r_motor, 55, 135)
base.settings(straight_acceleration=200)

def get_coeff(num):
    if num >= 0:
        return 1
    else:
        return -1

coeff = -1
angles = []
turn_sp = 0
turn_dir = 1
speed = 50
last_bool = False

s_motor.run_target(336, -30, then=Stop.HOLD, wait=True)

while True:
    if Button.CENTER in brick.buttons.pressed():
        break
    else:
        pass

while True:
    motor_angle = s_motor.angle()
    
    current_bool = color.reflection() < 20
    
    if current_bool != last_bool:
        if coeff == 1:
            angles.append(motor_angle + 5)
        else:
            angles.insert(0, motor_angle + 5)
    else:
        pass
    
    last_bool = current_bool 
        
    if abs(motor_angle) >= 80 and motor_angle * coeff > 0:

        if len(angles) >= 2:
            angle = angles[0]
            turn_dir = get_coeff(angle)
            turn_sp = (abs(angle) ** 1.4) / 5 * turn_dir #try 1.51 / 10 and 1.75 / 30
            speed = (200 / (2 + (1.6 ** (1 * abs(angle) - 20)))) + 50
            base.drive(speed, turn_sp)
        else:
            base.drive(50, turn_sp)
        
        coeff *= -1
        angles = []
    else:
        pass

    s_motor.track_target(90 * coeff)