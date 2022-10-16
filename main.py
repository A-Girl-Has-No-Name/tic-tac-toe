import pygame
import board
import colors


if __name__ == '__main__':
    A = board.Board(size=600, n=3)
    A.draw()
    B = board.Board(size=600, n=4)
    B.draw()
    C = board.Board(size=800, n=5)
    C.draw()
