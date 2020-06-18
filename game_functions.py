import pygame as pg

class GameFunctions():
    """
all the game's functions
"""
    def load_images(self):
        pieces = ['wP','wR','wN','wB','wQ','wK','bP','bR','bN','bB','bQ','bK']
        for piece in pieces:
            images[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"),(square_size,square_size))
        # we can access an image by saying images['wp']

        def c():
            print("hi")

