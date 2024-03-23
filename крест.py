import pygame

pygame.init()
w = int(input())
h = int(input())
win = pygame.display.set_mode((w, h))
win.fill((255,255,0))
pygame.draw.line(win, (255,255,255),(0,0),(w,h),5)
pygame.draw.line(win, (255,255,255),(0,w),(w,0),5)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
