import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

x = 250
y = 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= 4
    elif keys[pygame.K_d]:
        x += 4
    elif keys[pygame.K_w]:
        y -= 4
    elif keys[pygame.K_s]:
        y += 4
    elif keys[pygame.K_a] and keys[pygame.K_w]:
        x -= 4
        y -= 4
    elif keys[pygame.K_a] and keys[pygame.K_s]:
        x -= 4
        y += 4
    elif  keys[pygame.K_d] and keys[pygame.K_w]:
        y -= 4
        x += 4
    elif keys[pygame.K_d] and keys[pygame.K_s]:
        x += 4
        y += 4
    else:
        win.fill((255, 255, 255))
        if x < 250:
            x += 4
        elif x > 250:
            x -= 4
        if y < 250:
            y += 4
        elif y > 250:
            y -= 4
    if x > 400 or y > 400 or x < 100 or y < 100:
        win.fill((255, 255, 255))
        pygame.draw.circle(win, (4 % 255,2 * 4 % 25,3 * 4 % 2), (x, y), 30)
        pygame.display.update()
        pygame.time.delay(10)
    else:
        win.fill((255, 255, 255))
        pygame.draw.circle(win, (255, 0, 255), (x, y), 30)
        pygame.display.update()

    pygame.time.delay(20)
