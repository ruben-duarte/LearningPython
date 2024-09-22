from vpython import *

#Simulacion de pendulo
#swinging pendulum

GRAVITY = 9.8
LENGTH_PENDULUM = 1
theta = 15*pi/180 #radians
#theta_dot
angular_velocity = 0

# time and delta t : dt
time = 0
dt =0.01

top_pivot_point = sphere(pos=vector(0,LENGTH_PENDULUM/2,0), radius=LENGTH_PENDULUM/30)

mass = sphere(pos=top_pivot_point.pos + LENGTH_PENDULUM*vector(sin(theta), -cos(theta),0),radius=LENGTH_PENDULUM/15, color=color.green, make_trail=True)

string = cylinder(pos = top_pivot_point.pos, axis=mass.pos - top_pivot_point.pos, radius=LENGTH_PENDULUM/100)

while time < 18 : #secs
    rate(100)
    angular_aceleration = -GRAVITY*sin(theta)/LENGTH_PENDULUM
    angular_velocity = angular_velocity + angular_aceleration * dt
    theta += angular_velocity*dt
    time += dt
    mass.pos = top_pivot_point.pos + LENGTH_PENDULUM*vector(sin(theta), -cos(theta), 0)
    string.axis = mass.pos - top_pivot_point.pos
     

while True:
    pass