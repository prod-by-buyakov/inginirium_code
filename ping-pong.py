import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))


class Circle:

    def __init__(self, x, y, color, rad):
        self.x = x
        self.y = y
        self.color = color
        self.rad = rad
        self.velocity= 30
        self.is_jump = False

    def move_by_keys(self):
        if self.is_jump:
            if self.velocity >= -30:
                self.y -= self.velocity
                self.velocity -= 30
            else:
                self.is_jump = False
                self.velocity = 30
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.x += 3
        elif keys[pygame.K_UP]:
            self.y -= 3
        elif keys[pygame.K_DOWN]:
            self.y += 3
        if keys[pygame.K_SPACE]:
            self.is_jump = True




    def draw(self, root):
        pygame.draw.circle(root, self.color, (self.x, self.y), self.rad)


c = Circle(250, 250, (255, 255, 0), 30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))
    c.draw(win)
    c.move_by_keys()
    pygame.display.update()
    pygame.time.delay(10)
