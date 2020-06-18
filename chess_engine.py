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