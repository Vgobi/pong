import pgzrun
#import Palette
from pgzero.actor import Actor
from random import randint, choice

class Palette():
    def __init__(self, palette, posicion):
        """Palette i jej właściwości"""
        self.palette = palette
        self.palette.x = posicion[0]
        self.palette.y = posicion[1]
        self.palette.speed = 5

    def drawing(self):
        self.palette.draw()

    def move(self, direction):
        if direction == "left":
            self.palette.x -= self.palette.speed
            if self.palette.x < 70:
                self.palette.x = 75
        elif direction == "right":
            self.palette.x += self.palette.speed
            if self.palette.x > (WIDTH - 70):
                self.palette.x = WIDTH - 75

def update_ball_position():
    #aktualna pozycja na osi x
    if ball.direction_x == "left":
        ball.x -= ball.speed
    elif ball.direction_x == "right":
        ball.x += ball.speed

    #aktualna pozycja na osi y
    if ball.direction_y =="up":
        ball.y -= ball.speed
    elif ball.direction_y =="down":
        ball.y += ball.speed

    #sprawdzanie czy piłeczka odbije się od krawędzi okna
    if ball.x < 5:
        ball.direction_x == "right"
    elif ball.x < WIDTH - 5:
        ball.direction_x == "left"

    #sprawdzanie czy ktoś wygrał
    if ball.y < 5:
        ball.winner = "gracz_b"
    elif ball.y > HEIGHT - 5:
        ball.winner = "gracz a"

#start programu
WIDTH = 1280
HEIGHT = 800
TITLE = "SEX PONG"

#stary kod od palettek
#stary kod
#Definiujemy wyswietlane obiekty
# palette_a = Actor("palette.png")
# palette_a.y = 10
# palette_a.x = randint(70, 1210)
# palette_b = Actor("palette.png")
# palette_b.y = 790
# palette_b.x = randint(70, 1210)
ball = Actor("ball.png")
ball.y = HEIGHT//2
ball.x = WIDTH//2

#definiujemy własne własciwosci#

palette_a = Palette(Actor("palette.png"), (randint(70, 1210), 10))
palette_b = Palette(Actor("palette.png"), (randint(70, 1210), 790))

ball.direction_x = choice(("left", "right"))
ball.direction_y = choice(("up", "down"))
ball.winner = None
ball.speed = 1


def update_palettes():
    #gracz a
    if keyboard.a:
        palette_a.move("left")
    elif keyboard.s:
        palette_a.move("right")
    #gracz b
    if keyboard.k:
        palette_b.move("left")
    elif keyboard.l:
        palette_b.move("right")

def update():
    update_ball_position()
    update_palettes()


def draw():

    screen.blit("background.jpg", (0, 0))
    palette_a.drawing()
    palette_b.drawing()
    ball.draw()

pgzrun.go()
