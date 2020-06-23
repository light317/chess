"""
this class is responsible for all of the chess games logic and storing data
"""

class GameState():
    def __init__(self):
        self.board = [["bR","bN","bB","bQ","bK","bB","bN","bR"],
                      ["bP","bP","bP","bP","bP","bP","bP","bP"],
                      ["  ","  ","  ","  ","  ","  ","  ","  "],
                      ["  ","  ","  ","  ","  ","  ","  ","  "],
                      ["  ","  ","  ","  ","  ","  ","  ","  "],
                      ["  ","  ","  ","  ","  ","  ","  ","  "],
                      ["wP","wP","wP","wP","wP","wP","wP","wP"],
                      ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.whiteToMove = True
        self.moveLog = []


class Move():
    # varriables to convert between chess notations and regular array notations

    ranks_to_rows = {"1":7,"2":6,"3":5,"4":4,
                     "5":3,"6":2,"7":1,"8":0}

    rows_to_ranks = {v: k for k,v in ranks_to_rows.items()}

    files_to_col = {"a":0,"b":1,"c":2,"d":3,
                    "e":4,"f":5,"g":6,"h":7}

    rows_to_raks = {v: k for k,v in files_to_col.items()}

    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]
        self.piece_moved = board[self.start_row,self.start_col]
        self.piece_captured = board[self.end_row, self.end_col]

    def getChessNotation(self):
        pass