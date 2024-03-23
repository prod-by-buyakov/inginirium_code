import random

import pygame

W, H = 600, 600
pygame.init()
win = pygame.display.set_mode((W, H))


class Direction:
    x = 1
    y = 1


class Figura:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choices(range(256), k=3)
        self.dir = Direction()

    def move(self):
        self.x += self.dir.x * 3
        self.y -= self.dir.y * 3
        if self.x < 0 or self.x > W:
            self.dir.x *= -1
        if self.y < 0 or self.y > H:
            self.dir.y *= -1

    def draw(self, root):
        pass


class Circle(Figura):
    def __init__(self, x, y, rad):
        super().__init__(x, y)
        self.rad = rad

    def draw(self, root):
        pygame.draw.circle(root, self.color, (self.x, self.y), self.rad)


class Rect(Figura):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def draw(self, root):
        pygame.draw.rect(root, self.color, (self.x, self.y, self.w, self.h))


figures = [random.choice((
    Circle(random.randint(0, W), random.randint(0, H), random.randint(20, 50)),
    Rect(random.randint(0, W), random.randint(0, H), random.randint(10, 50), random.randint(10, 50))))
    for _ in range(50)]
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255,) * 3)
    for figura in figures:
        figura.move()
        figura.draw(win)
    pygame.display.update()
    pygame.time.delay(10)
