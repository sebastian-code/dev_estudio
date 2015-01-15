'''
Created on 14/10/2013
@summary: Aplicacion creada a manera de ejercicio para afianzar conocimientos.
@author: Sebastian Reyes Espinosa.
@version: v1
'''
from swampy.TurtleWorld import *
import math

ventana = TurtleWorld()
bob = Turtle()

def square(t, length):
    print t
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
        
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

circle(bob, 100)
wait_for_user()