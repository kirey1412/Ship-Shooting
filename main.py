import pgzrun, random

TITLE="Ship Shooting"
WIDTH=700
HEIGHT=560

speed=5

bullets=[]
enemies=[]

score=0
ship=Actor("ship.png")
enemy=Actor("bug.png")

enemies.append(enemy)

enemies[-1].x=10 #to update recently added element
enemies[-1].y=-100

def draw():
    screen.clear()
    screen.fill("lightpink")
    ship.draw()
    for i in enemies:
        i.draw()
    screen.draw.text(str(score), (50,50), color="navy")

def update():
    global score
    if keyboard.left:
        ship.x-=speed
    elif keyboard.right:
        ship.x+=speed