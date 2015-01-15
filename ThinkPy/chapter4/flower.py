'''
Created on 14/10/2013
@summary: Aplicacion creada a manera de ejercicio para afianzar conocimientos.
@author: Sebastian Reyes Espinosa.
@version: v1
'''
from swampy.TurtleWorld import *
# from TurtleWorld import *
from polygon import *


def petal(t, r, angle):
    """
    Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)


def flower(t, n, r, angle):
    """
    Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)


def move(t, length):
    """
    Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# Dibuja una secuencia de tres flores.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

die(bob)

# crea el archivo canvas.eps con el contenido del dibujo creado con Bob
world.canvas.dump()

wait_for_user()
