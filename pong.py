import pgzrun
#import Palette
from pgzero.actor import Actor
from random import randint, choice

class Palette():
    def __init__(self, palette, posicion, width=140, ball_width=10):
        """Palette i jej właściwości"""
        self.palette = palette
        self.palette.x = posicion[0]
        self.palette.y = posicion[1]
        self.palette.speed = 5
        self.palette.pcenter = width//2
        self.palette.ball_width = ball_width

    def drawing(self):
        self.palette.draw()

    def move(self, direction):
        if direction == "left":
            self.palette.x -= self.palette.speed
            if self.palette.x < self.palette.pcenter:
                self.palette.x = self.palette.pcenter + 5
        elif direction == "right":
            self.palette.x += self.palette.speed
            if self.palette.x > (WIDTH - self.palette.pcenter):
                self.palette.x = WIDTH - self.palette.pcenter + 5

    def bounce(self):
        if (
                self.palette.distance_to(ball) > self.palette.pcenter + self.palette.ball_width)\
                :
            return False

        if abs(self.palette.y - ball.y) > self.palette.ball_width * 2:
            return False

        if self.palette.x > ball.x and ball.direction_x == "left":
            ball.direction_x = "right"
        elif self.palette.x > ball.x and ball.direction_x == "right":
            ball.direction_x = "left"

        return True

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
        ball.direction_x = "right"
    elif ball.x > WIDTH - 5:
        ball.direction_x = "left"

    #sprawdzanie czy ktoś wygrał
    if ball.y < 5:
        ball.winner = "gracz_b"
    elif ball.y > HEIGHT - 5:
        ball.winner = "gracz a"

def check_bounce():
    if palette_a.bounce():
        ball.direction_y = "down"
    if palette_b.bounce():
        ball.direction_y = "up"

def check_winner():
    if ball.winner:
        winner_txt = f"Fuck the winner: {ball.winner}"
        screen.draw.text(
            winner_txt, (WIDTH//3 , HEIGHT // 2), color="yellow", fontsize=30
        )

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
    check_bounce()


def draw():

    screen.blit("background.jpg", (0, 0))
    palette_a.drawing()
    palette_b.drawing()
    ball.draw()
    check_winner()

pgzrun.go()
