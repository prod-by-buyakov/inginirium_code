import pygame

BLACK = (0,) * 3
GRAY = (100,) * 3
WHITE = (255,) * 3
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

CROSS = '#046582'
CIRCLE = '#e4bad4'

pygame.init()

FPS = 30
W, H = 600, 600

win = pygame.display.set_mode((W, H))
pygame.display.set_caption('TIC TAC TOE!)')


def draw_circle(sc, x, y, size):
    x = (x + .5) * size
    y = (y + .5) * size
    pygame.draw.circle(sc, CIRCLE, (x, y), (size - 3) // 2, 3)


def draw_cross(sc, x, y, size):
    x = x * size + 3
    y = y * size + 3
    pygame.draw.line(sc, CROSS, (x, y), (x + size - 3, y + size - 3), 3)
    pygame.draw.line(sc, CROSS, (x + size - 3, y - 3), (x, y + size - 3), 3)


def is_end(board):
    check_i_line = lambda x, i: x[i][0] == x[i][1] == x[i][2] != 0
    check_i_col = lambda x, i: x[0][i] == x[1][i] == x[2][i] != 0
    check_main_diag = lambda x: x[0][0] == x[1][1] == x[2][2] != 0
    check_secondary_diag = lambda x: x[0][2] == x[1][1] == x[2][0] != 0
    for i in range(3):
        if check_i_col(board, i):
            return 'col', i
        if check_i_line(board, i):
            return 'line', i
    if check_main_diag(board):
        return 'diag', 1
    if check_secondary_diag(board):
        return 'diag', 2
    return None


class Board:
    def __init__(self, w, h, size):
        self.w, self.h = w, h
        self.size = size
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.move = 1

    def click(self, mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size
        self.board[y][x] = self.move
        self.move = -self.move

    def check_end(self):
        is_end_info = is_end(self.board)
        shift = self.w // 10
        if is_end_info is not None:
            type_end = is_end_info[0]
            number = is_end_info[1]
            if type_end == 'col':
                x0 = (number + .5) * self.size
                y0 = shift
                x1 = x0
                y1 = self.h - shift

            elif type_end == 'line':
                x0 = shift
                y0 = (number + .5) * self.size
                x1 = self.w - shift
                y1 = y0
            elif type_end == 'diag':
                if number == 1:
                    x0 = shift
                    y0 = shift
                    x1 = self.w - shift
                    y1 = self.h - shift
                elif number == 2:
                    x0 = self.w - shift
                    y0 = shift
                    x1 = shift
                    y1 = self.h - shift
            pygame.draw.line(win, RED, (x0, y0), (x1, y1), 10)
            pygame.display.update()
            pygame.time.delay(3000)
            return True
        else:
            return False

    def render(self, screen):
        pygame.draw.line(screen, GRAY, (0, 200), (self.w, 200))
        pygame.draw.line(screen, GRAY, (0, 400), (self.w, 400))
        pygame.draw.line(screen, GRAY, (200, 0), (200, self.h))
        pygame.draw.line(screen, GRAY, (400, 0), (400, self.h))
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 1:
                    draw_cross(screen, x, y, self.size)
                elif self.board[y][x] == -1:
                    draw_circle(screen, x, y, self.size)


board = Board(W, H, 200)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.click(event.pos)
    win.fill(WHITE)
    board.render(win)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] or board.check_end():
        pygame.quit()
        exit()
