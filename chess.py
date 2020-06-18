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
    screen.fill(pg.Color('white'))
    gs = ChessEngine.GameState()
    load_images() #called only once thats why it is beofre the main loop
    game_running = True
    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False
        draw_game_state(screen,gs)
        clock.tick(max_fps)
        pg.display.flip()


"""
responsible for all graphics within the current game state
"""

def draw_game_state(screen, gs):
    draw_board(screen)
    #add in piece highlighting later
   # draw_pieces(screen,gs.board)

"""
draws the squares of the board
"""
def draw_board(screen):
    colors = [pg.Color('white'),pg.Color('dark-gray')]
    for r in range(dimedimension):
        for c in rarange(dimension):
            color = colors[((r+c)%2)]
            pg.draw.rect(screen,color,pg.Rect(c*square_size, r*square_size, square_size, square_size)


#def draw_pieces(screen,board):
#    pass

if __name__ == "__main__":
    main()