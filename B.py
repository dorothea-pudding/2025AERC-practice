from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from time import sleep

#建立參數
kp = 1
ki = 75
kd = 0.001
dt = 0.001
de = 0
x = 0
e = 0
up = 0
ui = 0
ud = 0
csL = ColorSensor(INPUT_1)
csR = ColorSensor(INPUT_2)
us = UltrasonicSensor(INPUT_4)
turn = 0
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
run = True
a = 0

#PID迴圈
while run == True:
    e = csL - csR - 2
    up = kp * e
    x = ( e * dt ) / de
    ui = ki * x
    ud = ( e * de ) / dt
    de = e
    turn = up + ui + ud
    steer_pair.on(steering=turn, speed=40)

    #雙黑
    if csL <= 20 and csL <= 20 :
        

    #避障
    if us <= 30 :
        steer_pair.on(steering = -40, speed = 40, seconds = 1)
        steer_pair.on(steering = 0, speed = 40, seconds = 1)
        steer_pair.on(steering = 40, speed = 40, seconds = 0.6)
        steer_pair.on(steering = 0, speed = 40, seconds = 0.65)
        steer_pair.on(steering = 40, speed = 40, seconds = 1)
        if csL >= 25 or csR >= 25 :
            steer_pair.on(steering = 0, speed = 40)
        else :
            steer_pair.on(steering = -45, speed = 40, seconds = 0.7)
