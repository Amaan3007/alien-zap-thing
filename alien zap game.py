import pgzrun
from random import randint

TITLE="Amazing shot"
WIDTH=500
LENGTH=500

message=""

alien=Actor("alien")
def draw():
    screen.clear
    screen.fill(color=120,0,0))
    alien.draw()
    
    screen.draw.text(message,centre=[400])
    
def_place():
    alien.x=randint(50,WIDTH-50)
    alien.y=randint(50,WIDTH-50)
    
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="Brilliant beginning"
        place()
    else:
        message="Try again xx"
place()
pgzrun.go()