"""
main driver for the chess game
"""

import pygame as pg
import ChessEngine

pg.init()
width = height = 512
dimension = 8
square_size = height//dimension
max_fps = 15
images = {}

"""
initialize a global dictionary of images. this will be called exactly once in the main
"""

def load_images():
    pieces = ['wP','wR','wN','wB','wQ','wK','bP','bR','bN','bB','bQ','bK']
    for piece in pieces:
        images[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"),(square_size,square_size))
    # we can access an image by saying images['wp']


def main():
    screen = pg.display.set_mode((width,height))
    clock = pg.time.Clock()
    screen.fill(pg.Color('black'))
    gs = ChessEngine.GameState()
    load_images() #called only once thats why it is beofre the main loop
    game_running = True
    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

        clock.tick(max_fps)
        pg.display.flip()





if __name__ == "__main__":
    main()