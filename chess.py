"""
main driver for the chess game
"""

import pygame as pg
import chess_engine
import game_functions

pg.init()
width = height = 512
dimension = 8
square_size = height // dimension
max_fps = 15
images = {}

"""
initialize a global dictionary of images. this will be called exactly once in the main
"""

def loadImages():
    pieces = ['wP','wR','wN','wB','wQ','wK','bP','bR','bN','bB','bQ','bK']
    for piece in pieces:
        images[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"),(square_size,square_size))
    # we can access an image by saying images['wp']
def main():
    screen = pg.display.set_mode((width,height))
    clock = pg.time.Clock()
    gs = chess_engine.GameState()
    gf = game_functions.GameFunctions()
    validMoves = gs.getValidMoves()
    moveMade = False #flag variable for when a move is made

    screen.fill(pg.Color('white'))
    gf.loadImages(images, square_size)
    game_running = True
    selected_square = () # no squares selected initially, tuple {row,col}
    player_clicks = [] # keep track of the player clicks, (two tuples, [{4,3},{6,6}]
    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False
            #mouse hamdler
            elif event.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos() # (x,y) location of the mouse
                col = location[0] // square_size
                row = location[1] // square_size
                if selected_square == (row,col): # if the selected square is theame as the mouse click, reset it
                    selected_square = ()
                    player_clicks = []
                else:
                     selected_square = (row,col)
                     player_clicks.append(selected_square)
                if len(player_clicks) == 2:   #after 2 clicks
                   move = chess_engine.Move(player_clicks[0], player_clicks[1], gs.board)
                   print(move.getChessNotation())
                   if move in validMoves:
                       gs.makeMove(move)
                       moveMade = True
                   gs.makeMove(move)
                   selected_square = () # reset user clicks
                   player_clicks = []

            # key handlers
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_z: #undo when 'z' is pressed
                    gs.undoMove()
                    moveMade = True

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        gf.drawGameState(images, screen, gs.board, square_size, dimension)
        clock.tick(max_fps)
        pg.display.flip()


def mock():
    pass

if __name__ == "__main__":
    main()

