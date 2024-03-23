import pygame

pygame.init()
a = int(input())
n = int(input())

win = pygame.display.set_mode((a,a))
win.fill((255,255,255))


for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            pygame.draw.rect(win, (0, 0, 0), (i * a // n, j * a // n, a // n, a // n))
            pygame.display.update()

while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     exit()
