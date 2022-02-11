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
        elif direction == "right":
            self.palette.x += self.palette.speed





