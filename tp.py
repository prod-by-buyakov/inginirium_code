import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

x = 100
y = 100

yc = 1
xc = 1

y3 = 1
x3 = 500

x1 = 250
y1 = 10
dirr = 1
dirc = 1
dirc11 = 1
dirc12 = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    y1 = y1 + dirc
    x = x + dirr
    if x + 100 > 500:
        dirr = -1
    elif x < 0:
        dirr = 1

    if y1 + 30 > 500:
        dirc = -1
    elif y1 < 0:
        dirc = 1

    yc = yc + dirc12
    xc = xc + dirc12

    if xc + 30 > 500:
        dir12 = -1

    if yc + 30 > 500:
        dirc12 = -1

    if xc + 30 > 500:
        dir12 = -1



    y3 = y3 - dirc11
    x3 = x3 + dirc11

    if x3 + 30 > 500:
        dirc11 = -1

    if y3 + 30 > 500:
        dirc11 = 1

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (225, 255, 0), (x, y, 100, 150))
    pygame.draw.circle(win, (0, 255, 0), (x1, y1,), 30)
    pygame.draw.circle(win, (0, 100, 255), (xc, yc), 30)
    pygame.draw.circle(win, (0, 100, 255), (x3, y3), 30)
    pygame.display.update()

    pygame.time.delay(1)
