import pygame
import board
import colors


if __name__ == '__main__':
    A = board.Board(size=600, n=3, back_color=colors.white, grid_color=colors.black)
    A.draw()
