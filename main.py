#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, GyroSensor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Button, Direction, Stop, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
import math

# Init
brick = EV3Brick()
color = ColorSensor(Port.S2)
ultsonic = UltrasonicSensor(Port.S3)
l_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
r_motor = Motor(Port.C, positive_direction=Direction.CLOCKWISE)
s_motor = Motor(Port.D)
base = DriveBase(l_motor, r_motor, 55, 185)
base.settings(straight_acceleration=200)

