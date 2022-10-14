import pygame
import colors

pygame.init()


class Board:
    def __init__(self, size=300, n=3, back_color=colors.white, grid_color=colors.black, line=5):
        self.size = size
        self.n = n
        self.back_color = back_color
        self.grid_color = grid_color
        self.cells = [[(0, 0)]*n for _ in range(n)]
        self.line_width = line

    def draw(self):
        screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Tic-tac-toe")
        screen.fill(self.grid_color)
        self.side = (self.size - ((self.n + 1) * self.line_width)) // self.n

        for i in range(self.n):
            for j in range(self.n):
                left = self.line_width + i*(self.side + self.line_width)
                top = self.line_width + j*(self.side + self.line_width)
                self.cells[i][j] = (left, top)
                r = pygame.Rect(left, top, self.side, self.side)
                pygame.draw.rect(screen, self.back_color, r)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.update()
