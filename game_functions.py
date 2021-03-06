import pygame as pg

class GameFunctions():
    """
all the game's functions
"""
    def load_images(self, images, square_size):
        pieces = ['wP','wR','wN','wB','wQ','wK','bP','bR','bN','bB','bQ','bK']
        for piece in pieces:
            images[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"),(square_size,square_size))
        # we can access an image by saying images['wp']

    """
    responsible for all graphics within the current game state
    """
    def draw_game_state(self, images, screen, board, square_size,dimension):
        self.draw_board(screen, square_size, dimension)
        # add in piece highlighting later
        self.draw_pieces(images, screen, board, square_size, dimension)

    # draw_pieces(screen,gs.board)

    """
    draws the squares of the board
    """

    def draw_board(self, screen,square_size,dimension):
        colors = [pg.Color('white'), pg.Color('gray')]
        for r in range(dimension):
            for c in range(dimension):
                color = colors[((r + c) % 2)]
                pg.draw.rect(screen, color, pg.Rect(c * square_size, r * square_size, square_size, square_size))

    def draw_pieces(self, images, screen, board, square_size, dimension):
        for r in range(dimension):
            for c in range(dimension):
                piece = board[r][c]
                if piece != "  ":
                    screen.blit(images[piece], pg.Rect(c*square_size, r*square_size, square_size, square_size))


