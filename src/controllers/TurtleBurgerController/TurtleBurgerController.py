#!/usr/bin/python3
"""TurtleBurgerController controller."""
# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
# create the Robot instance.
# 创建机器人
robot = Robot()
# get the time step of the current world.
# 获取时间戳
timestep = int(robot.getBasicTimeStep())
# get the motor devices
# 获取左右两侧的电机
leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
# set the target position of the motors
# 设置电机的旋转弧度 10rad
leftMotor.setPosition(20.0)
rightMotor.setPosition(20.0)
# leftMotor.setPosition(float('inf'))
# rightMotor.setPosition(float('inf'))
# 设置电机的旋转速度 rad/s
# leftMotor.setVelocity(2)
# rightMotor.setVelocity(2)
# 主循环
while robot.step(timestep) != -1:
    pass