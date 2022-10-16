import pygame
import colors

pygame.init()


class Board:
    def __init__(self, size=300, n=3, back_color=colors.white, grid_color=colors.black, line=25):
        self.size = size
        self.n = n
        self.side = 0
        self.back_color = back_color
        self.grid_color = grid_color
        self.cells = [[0]*n for _ in range(n)]
        self.line_width = line
        self.player = 0

    def get_cell(self, pos):
        # last line
        if pos[0] >= self.size - self.line_width or pos[1] >= self.size - self.line_width:
            return None
        i = int(pos[0] // (self.side + self.line_width))
        j = int(pos[1] // (self.side + self.line_width))
        # if cell already filled
        if self.cells[i][j] != 0:
            return None
        # mouse clicked in grid, not particular cell
        cell = self.get_corner(i, j)
        if pos[0] < cell[0] or pos[1] < cell[1]:
            return None
        return i, j

    def get_corner(self, i, j):
        # get corner of cell without grid
        left = self.line_width + i * (self.side + self.line_width)
        top = self.line_width + j * (self.side + self.line_width)
        return left, top

    def print_o(self, i, j, color):
        left, top = self.get_corner(i, j)
        center = (left + self.side//2, top + self.side//2)
        radius = self.side // 3
        width = self.side // 10
        pygame.draw.circle(self.screen, color, center, radius, width)

    def print_x(self, i, j, color):
        left, top = self.get_corner(i, j)
        skip = self.side//6
        width = self.side//8
        pygame.draw.line(self.screen, color, (left+skip, top+skip), (left+self.side-skip, top+self.side-skip), width)
        pygame.draw.line(self.screen, color, (left+self.side-skip, top+skip), (left+skip, top+self.side-skip), width)

    def draw(self):
        self.screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Tic-tac-toe")
        self.screen.fill(self.grid_color)
        self.side = (self.size - ((self.n + 1) * self.line_width)) // self.n

        for i in range(self.n):
            for j in range(self.n):
                left, top = self.get_corner(i, j)
                r = pygame.Rect(left, top, self.side, self.side)
                pygame.draw.rect(self.screen, self.back_color, r)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    cell = self.get_cell(pos)
                    if cell is None:
                        break
                    #self.print_o(*cell, colors.blue)
                    self.print_x(*cell, colors.red)
                    break
            pygame.display.update()
